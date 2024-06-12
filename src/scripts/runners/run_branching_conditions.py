import pandas as pd
import prosimos.simulation_engine
from discovery.gateway_conditions.gateway_conditions import discover_gateway_conditions
from pix_framework.io.event_log import EventLogIDs
import os
import json
from log_distance_measures.n_gram_distribution import n_gram_distribution_distance
from statistics import mean
from scripts.generators.generate_branching_conditions_short import generate_branching_scenarios as generate_short
from scripts.generators.generate_branching_conditions_long import generate_branching_scenarios as generate_long
from scripts.generators.simulate_branching_conditions import simulate_all_branching_conditions

PROSIMOS_LOG_IDS = EventLogIDs(
    case="case_id",
    activity="activity",
    enabled_time="enable_time",
    start_time="start_time",
    end_time="end_time",
    resource="resource",
)


def generate_model_csv_tuples(csv_folder_path, range):
    tuples_list = []
    bpmn_paths = {
        'xor': './assets/basic_xor_condition_model.bpmn',
        'or': './assets/basic_or_condition_model.bpmn'
    }

    for i in range:
        for prefix in bpmn_paths:
            csv_path = os.path.join(csv_folder_path, f"_{i}_{prefix}/_{i}.csv")
            if os.path.exists(csv_path):
                tuples_list.append((bpmn_paths[prefix], csv_path))

    return tuples_list


def update_and_save_json(event_log_file, results, is_probability=False):
    base_name = os.path.splitext(os.path.basename(event_log_file))[0]
    suffix = '_prob' if is_probability else '_DAS'
    json_file_path = os.path.join(os.path.dirname(event_log_file), base_name + '.json')
    new_json_file_path = os.path.join(os.path.dirname(event_log_file), base_name + '_test' + suffix + '.json')

    updated_content = {}

    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            content = json.load(file)
            updated_content = content

            updated_content['gateway_branching_probabilities'] = results['gateway_branching_probabilities']
            updated_content['branch_rules'] = results['branch_rules']

            if is_probability:
                updated_content.pop('branch_rules', None)
                for gateway in updated_content['gateway_branching_probabilities']:
                    for probability in gateway['probabilities']:
                        probability.pop('condition_id', None)

    with open(new_json_file_path, 'w') as new_file:
        json.dump(updated_content, new_file, indent=4)

    print(f"Updated JSON saved to {new_json_file_path}")
    return new_json_file_path


def discover_and_print_for_files(file_paths, log_ids, metrics_out_dir=None):
    all_metrics = {}

    for file_path in file_paths:
        bpmn_model_path, event_log_path = file_path
        base_name = os.path.splitext(os.path.basename(event_log_path))[0]
        print(base_name)

        if base_name not in all_metrics:
            all_metrics[base_name] = {"condition_metrics": [], "probability_metrics": []}

        train_log_path = event_log_path.replace(".csv", "_train.csv")
        test_log_path = event_log_path.replace(".csv", "_test.csv")

        print(f"\nDISCOVERING {train_log_path}")
        result = discover_gateway_conditions(bpmn_model_path, train_log_path, log_ids=log_ids)

        test_log_size = pd.read_csv(test_log_path)['case_id'].nunique()

        condition_json_file_path = update_and_save_json(event_log_path, result)
        probability_json_file_path = update_and_save_json(event_log_path, result, is_probability=True)

        for i in range(0, 3):
            condition_csv_file_path = condition_json_file_path.rsplit('.', 1)[0] + '.csv'
            probability_csv_file_path = probability_json_file_path.rsplit('.', 1)[0] + '.csv'

            prosimos.simulation_engine.run_simulation(bpmn_model_path, condition_json_file_path, test_log_size, log_out_path=condition_csv_file_path)
            condition_metrics = test_discovered_log(test_log_path, condition_csv_file_path)

            prosimos.simulation_engine.run_simulation(bpmn_model_path, probability_json_file_path, test_log_size, log_out_path=probability_csv_file_path)
            probability_metrics = test_discovered_log(test_log_path, probability_csv_file_path)

            all_metrics[base_name]["condition_metrics"].append(condition_metrics)
            all_metrics[base_name]["probability_metrics"].append(probability_metrics)

    if metrics_out_dir:
        print("\nFinal Metrics:")
        save_metrics(all_metrics, metrics_out_dir)


def save_metrics(metrics, metrics_out_dir):
    averaged_metrics = {}

    for model, model_metrics in metrics.items():
        avg_cond_metrics = {}
        avg_prob_metrics = {}

        cond_metrics_list = model_metrics['condition_metrics']
        prob_metrics_list = model_metrics['probability_metrics']

        metric_names = set()
        for metrics_dict in cond_metrics_list + prob_metrics_list:
            metric_names.update(metrics_dict.keys())

        for metric_name in metric_names:
            cond_metric_values = [m[metric_name] for m in cond_metrics_list if metric_name in m]
            prob_metric_values = [m[metric_name] for m in prob_metrics_list if metric_name in m]

            if cond_metric_values:
                avg_cond_metrics[f'Cond_{metric_name}'] = mean(cond_metric_values)
            if prob_metric_values:
                avg_prob_metrics[f'Prob_{metric_name}'] = mean(prob_metric_values)

        averaged_metrics[model] = {**avg_cond_metrics, **avg_prob_metrics}

    data_for_df = []

    for model, avg_metrics in averaged_metrics.items():
        row = {'Model': model}
        row.update(avg_metrics)
        data_for_df.append(row)

    df = pd.DataFrame(data_for_df)

    csv_filename = 'simulation_metrics.csv'
    csv_path = f'{metrics_out_dir}/{csv_filename}'

    if os.path.exists(csv_path):
        df.to_csv(csv_path, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_path, mode='w', header=True, index=False)

    print(f'DataFrame saved to {csv_path}')


def convert_times(df):
    df['start_time'] = pd.to_datetime(df['start_time'], utc=True)
    df['end_time'] = pd.to_datetime(df['end_time'], utc=True)
    return df


def test_discovered_log(original_log_path, simulated_log_path):
    original_log = pd.read_csv(original_log_path)
    simulated_log = pd.read_csv(simulated_log_path)

    original_log = convert_times(original_log)
    simulated_log = convert_times(simulated_log)

    three_gram_distance = n_gram_distribution_distance(
        original_log, PROSIMOS_LOG_IDS,
        simulated_log, PROSIMOS_LOG_IDS,
        n=3
    )

    return {
        "three_gram_distance": three_gram_distance,
    }


def run_branching_conditions():
    generate_short()
    generate_long()
    simulate_all_branching_conditions()

    short_dependencies_path = './out/branching_conditions/short_term_dependencies'
    long_dependencies_path = './out/branching_conditions/long_term_dependencies'
    test_range = range(0, 100)

    # Short term dependencies discovery
    files_to_discover = generate_model_csv_tuples(short_dependencies_path, test_range)
    discover_and_print_for_files(files_to_discover, PROSIMOS_LOG_IDS, metrics_out_dir=short_dependencies_path)

    # Long term dependencies discovery
    files_to_discover = generate_model_csv_tuples(long_dependencies_path, test_range)
    discover_and_print_for_files(discover_gateway_conditions, files_to_discover, PROSIMOS_LOG_IDS, metrics_out_dir=long_dependencies_path)
