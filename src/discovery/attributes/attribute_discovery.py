import pandas as pd
import os
import csv
import xml.etree.ElementTree as ET
import logging
import warnings

from pix_framework.io.event_log import EventLogIDs
from discovery.attributes.helpers import subtract_lists, print_results_table, print_case_results_table
from discovery.attributes.preprocessing import preprocess_event_log
from discovery.attributes.ge_discrete_attributes import discover_global_and_event_discrete_attributes
from discovery.attributes.ge_continuous_attributes import discover_global_and_event_continuous_attributes
from discovery.attributes.case_attributes import discover_case_attributes
from discovery.attributes.metrics import get_metrics_by_type

warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

namespaces = {'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL'}


def discover_attributes(bpmn_model_path,
                        event_log_path,
                        log_ids: EventLogIDs,
                        avoid_columns: list = [],
                        confidence_threshold: float = 1.0,
                        metrics_folder = None):
    event_log = pd.read_csv(event_log_path)
    activity_ids = extract_bpmn_activity_ids(bpmn_model_path)
    event_log = replace_activity_names_with_ids(event_log, log_ids.activity, activity_ids)

    default_avoid_columns = [
        log_ids.case, log_ids.activity, log_ids.start_time,
        log_ids.end_time, log_ids.resource, log_ids.enabled_time
    ]
    avoid_columns = default_avoid_columns + avoid_columns

    attributes_to_discover = subtract_lists(event_log.columns, avoid_columns)

    g_dfs, e_dfs, encoders = preprocess_event_log(event_log, avoid_columns, log_ids)

    # CASE ATTRIBUTES
    case_attributes, case_attribute_metrics = discover_case_attributes(e_dfs, attributes_to_discover, encoders, log_ids, confidence_threshold)
    case_attribute_names = [attribute['name'] for attribute in case_attributes]
    attributes_to_discover = subtract_lists(attributes_to_discover, case_attribute_names)

    # DISCRETE GLOBAL AND EVENT ATTRIBUTES
    discrete_results = discover_global_and_event_discrete_attributes(g_dfs, e_dfs, attributes_to_discover, encoders)
    discrete_results = determine_attribute_type_and_best_model(discrete_results, "KS")
    global_discrete_attributes, event_discrete_attributes = format_attribute_results(discrete_results)

    discovered_discrete_attribute_names = get_discovered_attribute_names(global_discrete_attributes, event_discrete_attributes)
    attributes_to_discover = subtract_lists(attributes_to_discover, discovered_discrete_attribute_names)

    # CONTINUOUS GLOBAL AND EVENT ATTRIBUTES
    continuous_results = discover_global_and_event_continuous_attributes(g_dfs, e_dfs, attributes_to_discover)
    continuous_results = determine_attribute_type_and_best_model(continuous_results, "EMD")
    global_continuous_attributes, event_continuous_attributes = format_attribute_results(continuous_results)

    global_attributes = merge_global_attributes(global_discrete_attributes,
                                                global_continuous_attributes)

    event_attributes = merge_event_attributes(event_discrete_attributes,
                                              event_continuous_attributes)

    print_results_table(discrete_results, get_metrics_by_type("discrete"))
    print_results_table(continuous_results, get_metrics_by_type("continuous"))
    print_case_results_table(case_attribute_metrics)

    if metrics_folder:
        save_metrics_to_file(discrete_results, get_metrics_by_type("discrete"), metrics_folder, "metrics_discrete.csv")
        save_metrics_to_file(continuous_results, get_metrics_by_type("continuous"), metrics_folder, "metrics_continuous.csv")
        save_case_metrics_to_file(case_attribute_metrics, metrics_folder, "metrics_case.csv")

    return {
        "global_attributes": global_attributes,
        "case_attributes": case_attributes,
        "event_attributes": event_attributes
    }



def save_case_metrics_to_file(model_results, output_dir, file_name='case_metrics.csv'):
    discrete_metrics = get_metrics_by_type("discrete")
    continuous_metrics = get_metrics_by_type("continuous")

    discrete_attributes = {}
    continuous_attributes = {}

    for attr, metrics in model_results.items():
        if any(metric in discrete_metrics for metric in metrics.keys()):
            discrete_attributes[attr] = metrics
        else:
            continuous_attributes[attr] = metrics

    def save_attributes_to_file(attributes, title, writer):
        if not attributes:
            return

        metric_names = list(next(iter(attributes.values())).keys())
        header = ["Attribute"] + metric_names

        writer.writerow([title + " Case Attributes"])
        writer.writerow(header)

        for attr, metrics in attributes.items():
            row_values = [attr] + [metrics.get(metric, float('nan')) for metric in metric_names]
            writer.writerow(row_values)

    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, file_name)

    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',')

        save_attributes_to_file(discrete_attributes, "Discrete", writer)
        save_attributes_to_file(continuous_attributes, "Continuous", writer)

    print(f"Case metrics saved to {csv_path}")


def save_metrics_to_file(model_results, metric_names, output_dir, file_name='metrics.csv'):
    metric_labels = []
    for name in metric_names:
        metric_labels.extend([f"g_{name}", f"e_{name}", f"g_{name}_avg", f"e_{name}_avg", f"g_{name}_dev", f"e_{name}_dev"])

    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, file_name)

    file_exists = os.path.isfile(csv_path)

    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',')

        if not file_exists:
            header = ["Attribute", "Model", "Type"] + metric_labels
            writer.writerow(header)

        for attr, data in model_results.items():
            models_data = data['models']
            for model_name, model_data in models_data.items():
                total_scores = model_data.get('total_scores', {'global': {}, 'event': {}})
                attr_type = data.get('type', 'Undefined')
                model_name = model_name.replace(' ', '_')
                row_values = [attr, model_name, attr_type]

                for metric_name in metric_names:
                    g_score = total_scores['global'].get(metric_name, float('nan'))
                    e_score = total_scores['event'].get(metric_name, float('nan'))

                    g_mean = total_scores['global'].get(f'{metric_name}_avg', float('nan'))
                    e_mean = total_scores['event'].get(f'{metric_name}_avg', float('nan'))

                    g_deviation = total_scores['global'].get(f'{metric_name}_dev', float('nan'))
                    e_deviation = total_scores['event'].get(f'{metric_name}_dev', float('nan'))

                    row_values.extend([g_score, e_score, g_mean, e_mean, g_deviation, e_deviation])

                writer.writerow(row_values)

    print(f"Metrics saved to {csv_path}")


def determine_attribute_type_and_best_model(discovery_results, comparison_metric):
    for attr_name, attr_data in discovery_results.items():
        best_model_name = None
        best_score = None
        best_type = None

        for model_name, model_data in attr_data['models'].items():
            for attr_type in ['event', 'global']:
                if comparison_metric in model_data['total_scores'][attr_type]:
                    score = model_data['total_scores'][attr_type][comparison_metric]

                    if best_score is None or score < best_score:
                        best_score = score
                        best_model_name = model_name
                        best_type = attr_type

        if best_model_name and best_type:
            discovery_results[attr_name]['best_model'] = best_model_name
            discovery_results[attr_name]['type'] = best_type

    return discovery_results


def format_attribute_results(discovery_results):
    global_attributes = []
    event_attributes_dict = {}

    for attr_name, attr_data in discovery_results.items():
        best_model_name = attr_data.get('best_model')
        attr_type = attr_data.get('type')
        model_data = attr_data['models'][best_model_name]

        if best_model_name == 'Linear Regression' or best_model_name == 'Curve Fitting Update Rules':
            attribute_format = 'expression'
        elif best_model_name == 'M5Prime':
            attribute_format = 'dtree'
        elif best_model_name == 'Curve Fitting Generators':
            attribute_format = 'continuous'
        else:
            attribute_format = 'discrete'

        if attr_type == 'global':
            placeholder_values = {
                "distribution_name": "fix",
                "distribution_params": [{"value": 0}]} if attribute_format in ['continuous', 'expression', 'dtree'] \
                else [{"key": "", "value": 1}]

            global_attribute = {
                "name": attr_name,
                "type": 'continuous' if attribute_format in ['continuous', 'expression', 'dtree'] else 'discrete',
                "values": placeholder_values
            }
            if global_attribute not in global_attributes:
                global_attributes.append(global_attribute)

        for activity_id, activity_data in model_data['activities'].items():
            formula_info = activity_data[attr_type]['formula'] if attr_type in activity_data else None

            if formula_info:
                event_attribute_entry = {
                    "name": attr_name,
                    "type": attribute_format,
                    "values": formula_info
                }

                if activity_id not in event_attributes_dict:
                    event_attributes_dict[activity_id] = []
                event_attributes_dict[activity_id].append(event_attribute_entry)

    event_attributes = [{"event_id": event_id, "attributes": attrs} for event_id, attrs in
                        event_attributes_dict.items()]

    return global_attributes, event_attributes


def get_discovered_attribute_names(global_attrs, event_attrs):
    global_attr_names = [attr['name'] for attr in global_attrs]

    event_attr_names = []
    for event in event_attrs:
        for attr in event['attributes']:
            if attr['name'] not in event_attr_names:
                event_attr_names.append(attr['name'])

    discovered_attr_names = list(set(global_attr_names + event_attr_names))
    return discovered_attr_names


def merge_global_attributes(*global_attributes_groups):
    merged_global_attributes = []
    for attribute_group in global_attributes_groups:
        merged_global_attributes.extend(attribute_group)
    return merged_global_attributes


def merge_event_attributes(*event_attributes_groups):
    merged_events_dict = {}

    def merge_event_list(event_list):
        for event in event_list:
            event_id = event['event_id']
            if event_id not in merged_events_dict:
                merged_events_dict[event_id] = event['attributes']
            else:
                existing_attrs = {attr['name'] for attr in merged_events_dict[event_id]}
                merged_events_dict[event_id].extend(
                    [attr for attr in event['attributes'] if attr['name'] not in existing_attrs]
                )

    for event_group in event_attributes_groups:
        merge_event_list(event_group)

    merged_event_attributes = [{"event_id": event_id, "attributes": attrs} for event_id, attrs in merged_events_dict.items()]
    return merged_event_attributes


def extract_bpmn_activity_ids(bpmn_path):
    tree = ET.parse(bpmn_path)
    root = tree.getroot()

    activity_mapping = {}

    for task in root.findall('.//bpmn:task', namespaces):
        task_id = task.attrib['id']
        task_name = task.attrib['name']
        activity_mapping[task_name] = task_id

    return activity_mapping


def replace_activity_names_with_ids(log, activity_column, activity_mapping):
    log[activity_column] = log[activity_column].map(activity_mapping).fillna(log[activity_column])
    return log

