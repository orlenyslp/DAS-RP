import os
import re
import pandas as pd
import prosimos.simulation_engine
from sklearn.model_selection import train_test_split


def split_event_log(log_path):
    df = pd.read_csv(log_path)
    
    if 'case_id' not in df.columns:
        raise ValueError("The event log must contain a 'case_id' column.")
    
    case_ids = df['case_id'].unique()
    train_ids, test_ids = train_test_split(case_ids, test_size=0.5, random_state=42)
    
    train_log = df[df['case_id'].isin(train_ids)]
    test_log = df[df['case_id'].isin(test_ids)]
    
    train_log_path = log_path.replace(".csv", "_train.csv")
    test_log_path = log_path.replace(".csv", "_test.csv")
    
    train_log.to_csv(train_log_path, index=False)
    test_log.to_csv(test_log_path, index=False)
    
    print(f"Train log saved to: {train_log_path}")
    print(f"Test log saved to: {test_log_path}\n")
    

def simulate_branching_conditions(base_directory, simulate_range=None):
    pattern = re.compile(r"_(\d+)_(xor|or)")
    bpmn_files = {
        "xor": "./assets/basic_xor_condition_model.bpmn",
        "or": "./assets/basic_or_condition_model.bpmn"
    }

    for dir_name in os.listdir(base_directory):
        match = pattern.match(dir_name)
        if match and os.path.isdir(os.path.join(base_directory, dir_name)):
            index, condition_type = match.groups()
            index = int(index)

            if simulate_range is None or (index >= simulate_range[0] and index <= simulate_range[1]):
                print(f"Simulating dir: {dir_name}")
                bpmn_file_path = bpmn_files[condition_type]
                csv_file_path = os.path.join(base_directory, dir_name, f"_{index}.csv")
                json_file_path = os.path.join(base_directory, dir_name, f"_{index}.json")

                if os.path.exists(bpmn_file_path) and os.path.exists(json_file_path):
                    print(f"Running simulation for {bpmn_file_path} using {json_file_path}")
                    prosimos.simulation_engine.run_simulation(bpmn_file_path, json_file_path, 2000, log_out_path=csv_file_path)
                    split_event_log(csv_file_path)


def simulate_all_branching_conditions():
    short_dependencies_path = './out/branching_conditions/short_term_dependencies'
    long_dependencies_path = './out/branching_conditions/long_term_dependencies'
    simulate_range = (0, 41)
    simulate_branching_conditions(short_dependencies_path, simulate_range=simulate_range)
    simulate_branching_conditions(long_dependencies_path, simulate_range=simulate_range)
