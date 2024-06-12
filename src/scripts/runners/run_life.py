import pandas as pd
import prosimos.simulation_engine
from sklearn.model_selection import train_test_split

from discovery.attributes.attribute_discovery import discover_attributes
from pix_framework.io.event_log import EventLogIDs
import json
import os
from discovery.gateway_conditions.gateway_conditions import discover_gateway_conditions
from pix_framework.io.event_log import EventLogIDs
import pprint
import os
import json
from log_distance_measures.n_gram_distribution import n_gram_distribution_distance

PROSIMOS_LOG_IDS = EventLogIDs(
    case="case_id",
    activity="activity",
    enabled_time="enable_time",
    start_time="start_time",
    end_time="end_time",
    resource="resource",
)

REAL_LIFE_LOG_IDS = EventLogIDs(
    case="case_id",
    activity="activity",
    start_time="Start_Time",
    end_time="End_Time",
    resource="resource",
)


def count_cases_in_event_log(csv_path, case_id_column):
    event_log = pd.read_csv(csv_path)
    unique_cases = event_log[case_id_column].nunique()
    return unique_cases


def convert_times(df, log_ids):
    df[log_ids.start_time] = pd.to_datetime(df[log_ids.start_time], utc=True)
    df[log_ids.end_time] = pd.to_datetime(df[log_ids.end_time], utc=True)
    return df


def test_discovered_log(original_log_path, simulated_log_path):
    original_log = pd.read_csv(original_log_path)
    simulated_log = pd.read_csv(simulated_log_path)

    original_log = convert_times(original_log, REAL_LIFE_LOG_IDS)
    simulated_log = convert_times(simulated_log, PROSIMOS_LOG_IDS)

    three_gram_distance = n_gram_distribution_distance(
        original_log, REAL_LIFE_LOG_IDS,
        simulated_log, PROSIMOS_LOG_IDS,
        n=3
    )

    return {
        "three_gram_distance": three_gram_distance
    }


def save_metrics(metrics, outputdir):
    data_for_df = []

    trad_metrics = metrics['TRAD']
    cond_metrics = metrics['COND']

    row = dict()
    for metric_name in cond_metrics.keys():
        row[f'Cond_{metric_name}'] = cond_metrics.get(metric_name, 'N/A')
        row[f'Prob_{metric_name}'] = trad_metrics.get(metric_name, 'N/A')

    data_for_df.append(row)
    df = pd.DataFrame(data_for_df)

    csv_filename = 'simulation_metrics.csv'
    csv_path = os.path.join(outputdir, csv_filename)

    file_exists = os.path.exists(csv_path)
    df.to_csv(csv_path, mode='a', header=not file_exists, index=False)

    print(f'DataFrame saved to {csv_path}')


def run_life():
    assets_path = './assets'
    out_path = './out/real_life'
    real_life_experiments = [
        'BPIC2019',
        'Sepsis',
        'Trafic'
    ]

    for experiment in real_life_experiments:
        bpmn_path = f"{assets_path}/{experiment}/{experiment}.bpmn"
        log_path = f"{assets_path}/{experiment}/{experiment}.zip"
        config_path = f"{assets_path}/{experiment}/{experiment}.json"

        experiment_out_path = f"{out_path}/{experiment}"
        train_path = f"{experiment_out_path}/{experiment}_train.csv"
        test_path = f"{experiment_out_path}/{experiment}_test.csv"

        trad_config_path = f"{experiment_out_path}/{experiment}_TRAD.json"
        cond_config_path = f"{experiment_out_path}/{experiment}_COND.json"
        trad_log_path = f"{experiment_out_path}/{experiment}_TRAD.csv"
        cond_log_path = f"{experiment_out_path}/{experiment}_COND.csv"

        # Create out dir for real life logs
        os.makedirs(experiment_out_path, exist_ok=True)

        # Train test split
        log = pd.read_csv(log_path, compression="zip")
        log_train, log_test = train_test_split(log, test_size=0.5, random_state=42)
        log_train.to_csv(train_path, index=False)
        log_test.to_csv(test_path, index=False)
        print(f"Split {log_path}: train ({len(log_train)}) and test ({len(log_test)})")

        with open(config_path, 'r') as config_file:
            trad_config = json.load(config_file)
        with open(config_path, 'r') as config_file:
            cond_config = json.load(config_file)

        # Discover attributes for DAS model
        attributes = discover_attributes(bpmn_path, log_path, log_ids=REAL_LIFE_LOG_IDS, metrics_folder=experiment_out_path)
        cond_config.update(attributes)

        # Discover conditions for DAS model
        conditions = discover_gateway_conditions(bpmn_path, log_path, REAL_LIFE_LOG_IDS)
        cond_config['gateway_branching_probabilities'] = conditions['gateway_branching_probabilities']
        cond_config['branch_rules'] = conditions['branch_rules']

        # Write config files for both models
        with open(trad_config_path, 'w') as trad_config_file:
            json.dump(trad_config, trad_config_file, indent=4)
        with open(cond_config_path, 'w') as cond_config_file:
            json.dump(cond_config, cond_config_file, indent=4)

        # Run Simulations
        cases_amount = count_cases_in_event_log(test_path, REAL_LIFE_LOG_IDS.case)
        prosimos.simulation_engine.run_simulation(bpmn_path, trad_config_path, cases_amount, log_out_path=trad_log_path)
        prosimos.simulation_engine.run_simulation(bpmn_path, cond_config_path, cases_amount, log_out_path=cond_log_path)

        # Test models
        metrics = {
            "TRAD": test_discovered_log(test_path, trad_log_path),
            "COND": test_discovered_log(test_path, cond_log_path)
        }

        save_metrics(metrics, experiment_out_path)
