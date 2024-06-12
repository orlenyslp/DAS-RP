import json
import copy
import os


def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json_file(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def generate_configs(template_file, modifications, output_prefix, start_index):
    template = load_json_file(template_file)
    for i, key in enumerate(modifications.keys(), start=start_index):
        mod = modifications[key]
        new_config = copy.deepcopy(template)
        if mod.get('branch_rules') is not None:
            new_config['branch_rules'] = mod['branch_rules']
        if mod.get('event_attributes') is not None:
            new_config['event_attributes'] = mod['event_attributes']
        if mod.get('global_attributes') is not None:
            new_config['global_attributes'] = mod['global_attributes']
        if mod.get('case_attributes') is not None:
            new_config['case_attributes'] = mod['case_attributes']
        directory = out_dir + f"./_{i}_{output_prefix}"
        filename = f"_{i}.json"
        file_path = os.path.join(directory, filename)
        save_json_file(file_path, new_config)


modifications_xor = {
    "pure_discrete_equal": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A5"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B4"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B5"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C4"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 0.2}, 
                                                                          {"key": "A2", "value": 0.2},
                                                                          {"key": "A3", "value": 0.2},
                                                                          {"key": "A4", "value": 0.2},
                                                                          {"key": "A5", "value": 0.2}]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0.2}, 
                                                                          {"key": "B2", "value": 0.2},
                                                                          {"key": "B3", "value": 0.2},
                                                                          {"key": "B4", "value": 0.2},
                                                                          {"key": "B5", "value": 0.2}]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0.2}, 
                                                                          {"key": "C2", "value": 0.2},
                                                                          {"key": "C3", "value": 0.2},
                                                                          {"key": "C4", "value": 0.2},
                                                                          {"key": "C5", "value": 0.2}]}]},    
        ]
    },

    "hybrid_20_discrete_equal": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A5"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B4"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B5"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C4"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 0.16}, 
                                                                          {"key": "A2", "value": 0.16},
                                                                          {"key": "A3", "value": 0.16},
                                                                          {"key": "A4", "value": 0.16},
                                                                          {"key": "A5", "value": 0.16}, 
                                                                          {"key": "X", "value": 0.2}]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0.16}, 
                                                                          {"key": "B2", "value": 0.16},
                                                                          {"key": "B3", "value": 0.16},
                                                                          {"key": "B4", "value": 0.16},
                                                                          {"key": "B5", "value": 0.16},
                                                                          {"key": "Y", "value": 0.2}]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0.16}, 
                                                                          {"key": "C2", "value": 0.16},
                                                                          {"key": "C3", "value": 0.16},
                                                                          {"key": "C4", "value": 0.16},
                                                                          {"key": "C5", "value": 0.16},
                                                                          {"key": "Z", "value": 0.2}]}]},    
        ]
    },


    "pure_discrete_unbalanced": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A5"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B4"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B5"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C4"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 1}, 
                                                                          {"key": "A2", "value": 0},
                                                                          {"key": "A3", "value": 0},
                                                                          {"key": "A4", "value": 0},
                                                                          {"key": "A5", "value": 0}
                                                                          ]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0}, 
                                                                          {"key": "B2", "value": 0},
                                                                          {"key": "B3", "value": 1},
                                                                          {"key": "B4", "value": 0},
                                                                          {"key": "B5", "value": 0}
                                                                          ]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0}, 
                                                                          {"key": "C2", "value": 0},
                                                                          {"key": "C3", "value": 0},
                                                                          {"key": "C4", "value": 0},
                                                                          {"key": "C5", "value": 1}
                                                                          ]}]},    
        ]
    },

    "hybrid_20_discrete_unbalanced": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A5"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B4"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B5"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C4"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 0.8}, 
                                                                          {"key": "A2", "value": 0},
                                                                          {"key": "A3", "value": 0},
                                                                          {"key": "A4", "value": 0},
                                                                          {"key": "A5", "value": 0},
                                                                          {"key": "X", "value": 0.2}
                                                                          ]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0}, 
                                                                          {"key": "B2", "value": 0},
                                                                          {"key": "B3", "value": 0.8},
                                                                          {"key": "B4", "value": 0},
                                                                          {"key": "B5", "value": 0},
                                                                          {"key": "Y", "value": 0.2}
                                                                          ]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0}, 
                                                                          {"key": "C2", "value": 0},
                                                                          {"key": "C3", "value": 0},
                                                                          {"key": "C4", "value": 0},
                                                                          {"key": "C5", "value": 0.8},
                                                                          {"key": "Z", "value": 0.2}
                                                                          ]}]},    
        ]
    },



    "pure_discrete_random": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A5"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B4"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B5"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C4"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 0.1}, 
                                                                          {"key": "A2", "value": 0.3},
                                                                          {"key": "A3", "value": 0.2},
                                                                          {"key": "A4", "value": 0.3},
                                                                          {"key": "A5", "value": 0.1}
                                                                          ]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0.3}, 
                                                                          {"key": "B2", "value": 0.1},
                                                                          {"key": "B3", "value": 0.2},
                                                                          {"key": "B4", "value": 0.1},
                                                                          {"key": "B5", "value": 0.3}
                                                                          ]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0.2}, 
                                                                          {"key": "C2", "value": 0.1},
                                                                          {"key": "C3", "value": 0.4},
                                                                          {"key": "C4", "value": 0.1},
                                                                          {"key": "C5", "value": 0.2}
                                                                          ]}]},    
        ]
    },

    "hybrid_20_discrete_random": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A5"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B4"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B5"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C4"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 0.08}, 
                                                                          {"key": "A2", "value": 0.24},
                                                                          {"key": "A3", "value": 0.16},
                                                                          {"key": "A4", "value": 0.24},
                                                                          {"key": "A5", "value": 0.08},
                                                                          {"key": "X", "value": 0.2}
                                                                          ]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0.24}, 
                                                                          {"key": "B2", "value": 0.08},
                                                                          {"key": "B3", "value": 0.16},
                                                                          {"key": "B4", "value": 0.08},
                                                                          {"key": "B5", "value": 0.24},
                                                                          {"key": "Y", "value": 0.2}
                                                                          ]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0.16}, 
                                                                          {"key": "C2", "value": 0.08},
                                                                          {"key": "C3", "value": 0.32},
                                                                          {"key": "C4", "value": 0.08},
                                                                          {"key": "C5", "value": 0.16},
                                                                          {"key": "Z", "value": 0.2}
                                                                          ]}]},    
        ]
    },



    "pure_continuous_values_norm": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["81", "100"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
        ]
    },

    "hybrid_20_continuous_values_norm": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "16"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["21", "36"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["41", "56"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["61", "76"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["81", "96"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "16"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["21", "36"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["41", "56"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["61", "76"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["81", "96"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "16"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["21", "36"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["41", "56"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["61", "76"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["81", "96"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
        ]
    },




    "pure_continuous_values_exp": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["81", "100"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]}
        ]
    },

    "hybrid_20_continuous_values_exp": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "16"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["21", "36"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["41", "56"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["61", "76"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["81", "96"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "16"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["21", "36"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["41", "56"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["61", "76"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["81", "96"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "16"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["21", "36"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["41", "56"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["61", "76"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["81", "96"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]}
        ]
    },


    "pure_complex_conditions_2_or": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["0", "20"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["21", "40"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["41", "60"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["61", "80"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["81", "100"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A5"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["0", "20"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["21", "40"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["41", "60"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["61", "80"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B4"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["81", "100"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B5"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["0", "20"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["21", "40"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["41", "60"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["61", "80"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C4"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["81", "100"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g1_2", "type": "discrete", "values": [{"key": "A1", "value": 0.2}, {"key": "A2", "value": 0.2}, {"key": "A3", "value": 0.2},
                                                               {"key": "A4", "value": 0.2}, {"key": "A5", "value": 0.2}]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g2_2", "type": "discrete", "values": [{"key": "B1", "value": 0.2}, {"key": "B2", "value": 0.2}, {"key": "B3", "value": 0.2},
                                                               {"key": "B4", "value": 0.2}, {"key": "B5", "value": 0.2}]}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g3_2", "type": "discrete", "values": [{"key": "C1", "value": 0.2}, {"key": "C2", "value": 0.2}, {"key": "C3", "value": 0.2},
                                                               {"key": "C4", "value": 0.2}, {"key": "C5", "value": 0.2}]}]}
        ],
    },

    "hybrid_20_complex_conditions_2_or": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["0", "16"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["21", "36"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["41", "56"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["61", "76"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["81", "96"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A5"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["0", "16"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["21", "36"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["41", "56"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["61", "76"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B4"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["81", "96"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B5"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["0", "16"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["21", "36"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["41", "56"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["61", "76"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C4"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["81", "96"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g1_2", "type": "discrete", "values": [{"key": "A1", "value": 0.16}, {"key": "A2", "value": 0.16}, {"key": "A3", "value": 0.16},
                                                                 {"key": "A4", "value": 0.16}, {"key": "A5", "value": 0.16}, {"key": "X", "value": 0.2}]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g2_2", "type": "discrete", "values": [{"key": "B1", "value": 0.16}, {"key": "B2", "value": 0.16}, {"key": "B3", "value": 0.16},
                                                                 {"key": "B4", "value": 0.16}, {"key": "B5", "value": 0.16}, {"key": "Y", "value": 0.2}]}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g3_2", "type": "discrete", "values": [{"key": "C1", "value": 0.16}, {"key": "C2", "value": 0.16}, {"key": "C3", "value": 0.16},
                                                                 {"key": "C4", "value": 0.16}, {"key": "C5", "value": 0.16}, {"key": "Z", "value": 0.2}]}]}
        ],
    },




    "pure_complex_conditions_2_and": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": ">", "value": "0"}, {"attribute": "g1", "comparison": "<=", "value": "20"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": ">", "value": "20"}, {"attribute": "g1", "comparison": "<=", "value": "40"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": ">", "value": "40"}, {"attribute": "g1", "comparison": "<=", "value": "60"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": ">", "value": "60"}, {"attribute": "g1", "comparison": "<=", "value": "80"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": ">", "value": "80"}, {"attribute": "g1", "comparison": "<=", "value": "100"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": ">", "value": "0"}, {"attribute": "g2", "comparison": "<=", "value": "20"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": ">", "value": "20"}, {"attribute": "g2", "comparison": "<=", "value": "40"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": ">", "value": "40"}, {"attribute": "g2", "comparison": "<=", "value": "60"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": ">", "value": "60"}, {"attribute": "g2", "comparison": "<=", "value": "80"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": ">", "value": "80"}, {"attribute": "g2", "comparison": "<=", "value": "100"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": ">", "value": "0"}, {"attribute": "g3", "comparison": "<=", "value": "20"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": ">", "value": "20"}, {"attribute": "g3", "comparison": "<=", "value": "40"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": ">", "value": "40"}, {"attribute": "g3", "comparison": "<=", "value": "60"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": ">", "value": "60"}, {"attribute": "g3", "comparison": "<=", "value": "80"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": ">", "value": "80"}, {"attribute": "g3", "comparison": "<=", "value": "100"}]]}
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]}
        ],
    },

    "hybrid_20_complex_conditions_2_and": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": ">", "value": "0"}, {"attribute": "g1", "comparison": "<=", "value": "16"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": ">", "value": "20"}, {"attribute": "g1", "comparison": "<=", "value": "36"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": ">", "value": "40"}, {"attribute": "g1", "comparison": "<=", "value": "56"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": ">", "value": "60"}, {"attribute": "g1", "comparison": "<=", "value": "76"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": ">", "value": "80"}, {"attribute": "g1", "comparison": "<=", "value": "96"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": ">", "value": "0"}, {"attribute": "g2", "comparison": "<=", "value": "16"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": ">", "value": "20"}, {"attribute": "g2", "comparison": "<=", "value": "36"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": ">", "value": "40"}, {"attribute": "g2", "comparison": "<=", "value": "56"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": ">", "value": "60"}, {"attribute": "g2", "comparison": "<=", "value": "76"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": ">", "value": "80"}, {"attribute": "g2", "comparison": "<=", "value": "96"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": ">", "value": "0"}, {"attribute": "g3", "comparison": "<=", "value": "16"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": ">", "value": "20"}, {"attribute": "g3", "comparison": "<=", "value": "36"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": ">", "value": "40"}, {"attribute": "g3", "comparison": "<=", "value": "56"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": ">", "value": "60"}, {"attribute": "g3", "comparison": "<=", "value": "76"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": ">", "value": "80"}, {"attribute": "g3", "comparison": "<=", "value": "96"}]]}
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]}
        ],
    },


    "pure_complex_conditions_3_or": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["0", "20"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A1"}], [{"attribute": "g1_3", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["21", "40"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A2"}], [{"attribute": "g1_3", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["41", "60"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A3"}], [{"attribute": "g1_3", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["61", "80"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A4"}], [{"attribute": "g1_3", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["81", "100"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A5"}], [{"attribute": "g1_3", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["0", "20"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B1"}], [{"attribute": "g2_3", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["21", "40"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B2"}], [{"attribute": "g2_3", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["41", "60"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B3"}], [{"attribute": "g2_3", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["61", "80"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B4"}], [{"attribute": "g2_3", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["81", "100"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B5"}], [{"attribute": "g2_3", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["0", "20"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C1"}], [{"attribute": "g3_3", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["21", "40"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C2"}], [{"attribute": "g3_3", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["41", "60"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C3"}], [{"attribute": "g3_3", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["61", "80"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C4"}], [{"attribute": "g3_3", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["81", "100"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C5"}], [{"attribute": "g3_3", "comparison": "in", "value": ["81", "100"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g1_2", "type": "discrete", "values": [{"key": "A1", "value": 0.2}, {"key": "A2", "value": 0.2}, {"key": "A3", "value": 0.2},
                                                                 {"key": "A4", "value": 0.2}, {"key": "A5", "value": 0.2}]},
                { "name": "g1_3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g2_2", "type": "discrete", "values": [{"key": "B1", "value": 0.2}, {"key": "B2", "value": 0.2}, {"key": "B3", "value": 0.2},
                                                                 {"key": "B4", "value": 0.2}, {"key": "B5", "value": 0.2}]},
                { "name": "g2_3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},

            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g3_2", "type": "discrete", "values": [{"key": "C1", "value": 0.2}, {"key": "C2", "value": 0.2}, {"key": "C3", "value": 0.2},
                                                                 {"key": "C4", "value": 0.2}, {"key": "C5", "value": 0.2}]},
                { "name": "g3_3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
        ],
    },

    "hybrid_20_complex_conditions_3_or": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["0", "20"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A1"}], [{"attribute": "g1_3", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["21", "40"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A2"}], [{"attribute": "g1_3", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["41", "60"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A3"}], [{"attribute": "g1_3", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["61", "80"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A4"}], [{"attribute": "g1_3", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["81", "100"]}], [{"attribute": "g1_2", "comparison": "=", "value": "A5"}], [{"attribute": "g1_3", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["0", "20"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B1"}], [{"attribute": "g2_3", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["21", "40"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B2"}], [{"attribute": "g2_3", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["41", "60"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B3"}], [{"attribute": "g2_3", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["61", "80"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B4"}], [{"attribute": "g2_3", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["81", "100"]}], [{"attribute": "g2_2", "comparison": "=", "value": "B5"}], [{"attribute": "g2_3", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["0", "20"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C1"}], [{"attribute": "g3_3", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["21", "40"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C2"}], [{"attribute": "g3_3", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["41", "60"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C3"}], [{"attribute": "g3_3", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["61", "80"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C4"}], [{"attribute": "g3_3", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["81", "100"]}], [{"attribute": "g3_2", "comparison": "=", "value": "C5"}], [{"attribute": "g3_3", "comparison": "in", "value": ["81", "100"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g1_2", "type": "discrete", "values": [{"key": "A1", "value": 0.16}, {"key": "A2", "value": 0.16}, {"key": "A3", "value": 0.16},
                                                                 {"key": "A4", "value": 0.16}, {"key": "A5", "value": 0.16}, {"key": "X", "value": 0.2}]},
                { "name": "g1_3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g2_2", "type": "discrete", "values": [{"key": "B1", "value": 0.16}, {"key": "B2", "value": 0.16}, {"key": "B3", "value": 0.16},
                                                                 {"key": "B4", "value": 0.16}, {"key": "B5", "value": 0.16}, {"key": "Y", "value": 0.2}]},
                { "name": "g2_3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},

            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g3_2", "type": "discrete", "values": [{"key": "C1", "value": 0.16}, {"key": "C2", "value": 0.16}, {"key": "C3", "value": 0.16},
                                                                 {"key": "C4", "value": 0.16}, {"key": "C5", "value": 0.16}, {"key": "Z", "value": 0.2}]},
                { "name": "g3_3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
        ],
    },


    "pure_complex_conditions_3_and": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1_1", "comparison": ">", "value": "0"}, {"attribute": "g1_1", "comparison": "<=", "value": "50"}, {"attribute": "g1_2", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1_1", "comparison": ">", "value": "50"}, {"attribute": "g1_1", "comparison": "<=", "value": "100"}, {"attribute": "g1_2", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1_1", "comparison": ">", "value": "0"}, {"attribute": "g1_1", "comparison": "<=", "value": "33"}, {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1_1", "comparison": ">", "value": "33"}, {"attribute": "g1_1", "comparison": "<=", "value": "66"}, {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1_1", "comparison": ">", "value": "66"}, {"attribute": "g1_1", "comparison": "<=", "value": "100"}, {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2_1", "comparison": ">", "value": "0"}, {"attribute": "g2_1", "comparison": "<=", "value": "50"}, {"attribute": "g2_2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2_1", "comparison": ">", "value": "50"}, {"attribute": "g2_1", "comparison": "<=", "value": "100"}, {"attribute": "g2_2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2_1", "comparison": ">", "value": "0"}, {"attribute": "g2_1", "comparison": "<=", "value": "33"}, {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2_1", "comparison": ">", "value": "33"}, {"attribute": "g2_1", "comparison": "<=", "value": "66"}, {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2_1", "comparison": ">", "value": "66"}, {"attribute": "g2_1", "comparison": "<=", "value": "100"}, {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3_1", "comparison": ">", "value": "0"}, {"attribute": "g3_1", "comparison": "<=", "value": "50"}, {"attribute": "g3_2", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3_1", "comparison": ">", "value": "50"}, {"attribute": "g3_1", "comparison": "<=", "value": "100"}, {"attribute": "g3_2", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3_1", "comparison": ">", "value": "0"}, {"attribute": "g3_1", "comparison": "<=", "value": "33"}, {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3_1", "comparison": ">", "value": "33"}, {"attribute": "g3_1", "comparison": "<=", "value": "66"}, {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3_1", "comparison": ">", "value": "66"}, {"attribute": "g3_1", "comparison": "<=", "value": "100"}, {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]}
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g1_2", "type": "discrete", "values": [{"key": "A1", "value": 0.5}, {"key": "A2", "value": 0.5}]}
                ]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g2_2", "type": "discrete", "values": [{"key": "B1", "value": 0.5}, {"key": "B2", "value": 0.5}]}
                ]},

            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g3_2", "type": "discrete", "values": [{"key": "C1", "value": 0.5}, {"key": "C2", "value": 0.5}]}
                ]}
        ],
    },

    "hybrid_20_complex_conditions_3_and": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1_1", "comparison": ">", "value": "0"}, {"attribute": "g1_1", "comparison": "<=", "value": "40"}, {"attribute": "g1_2", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1_1", "comparison": ">", "value": "50"}, {"attribute": "g1_1", "comparison": "<=", "value": "90"}, {"attribute": "g1_2", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1_1", "comparison": ">", "value": "0"}, {"attribute": "g1_1", "comparison": "<=", "value": "26"}, {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1_1", "comparison": ">", "value": "33"}, {"attribute": "g1_1", "comparison": "<=", "value": "59"}, {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1_1", "comparison": ">", "value": "66"}, {"attribute": "g1_1", "comparison": "<=", "value": "92"}, {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2_1", "comparison": ">", "value": "0"}, {"attribute": "g2_1", "comparison": "<=", "value": "40"}, {"attribute": "g2_2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2_1", "comparison": ">", "value": "50"}, {"attribute": "g2_1", "comparison": "<=", "value": "90"}, {"attribute": "g2_2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2_1", "comparison": ">", "value": "0"}, {"attribute": "g2_1", "comparison": "<=", "value": "26"}, {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2_1", "comparison": ">", "value": "33"}, {"attribute": "g2_1", "comparison": "<=", "value": "59"}, {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2_1", "comparison": ">", "value": "66"}, {"attribute": "g2_1", "comparison": "<=", "value": "92"}, {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3_1", "comparison": ">", "value": "0"}, {"attribute": "g3_1", "comparison": "<=", "value": "40"}, {"attribute": "g3_2", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3_1", "comparison": ">", "value": "50"}, {"attribute": "g3_1", "comparison": "<=", "value": "90"}, {"attribute": "g3_2", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3_1", "comparison": ">", "value": "0"}, {"attribute": "g3_1", "comparison": "<=", "value": "26"}, {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3_1", "comparison": ">", "value": "33"}, {"attribute": "g3_1", "comparison": "<=", "value": "59"}, {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3_1", "comparison": ">", "value": "66"}, {"attribute": "g3_1", "comparison": "<=", "value": "92"}, {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]}
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g1_2", "type": "discrete", "values": [{"key": "A1", "value": 0.4}, {"key": "A2", "value": 0.4}, {"key": "X", "value": 0.2}]}
                ]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g2_2", "type": "discrete", "values": [{"key": "B1", "value": 0.4}, {"key": "B2", "value": 0.4}, {"key": "Y", "value": 0.2}]}
                ]},

            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g3_2", "type": "discrete", "values": [{"key": "C1", "value": 0.4}, {"key": "C2", "value": 0.4}, {"key": "Z", "value": 0.2}]}
                ]}
        ],
    },



    "pure_complex_conditions_2_and_for_2_or": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["0", "20"]},   {"attribute": "g1_2", "comparison": "=", "value": "A1"}],  [{"attribute": "g1_1", "comparison": "in", "value": ["21", "40"]}, {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["21", "40"]},  {"attribute": "g1_2", "comparison": "=", "value": "A1"}],  [{"attribute": "g1_1", "comparison": "in", "value": ["41", "60"]}, {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["41", "60"]},  {"attribute": "g1_2", "comparison": "=", "value": "A1"}],  [{"attribute": "g1_1", "comparison": "in", "value": ["61", "80"]}, {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["61", "80"]},  {"attribute": "g1_2", "comparison": "=", "value": "A1"}],  [{"attribute": "g1_1", "comparison": "in", "value": ["81", "100"]},{"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["81", "100"]}, {"attribute": "g1_2", "comparison": "=", "value": "A1"}],  [{"attribute": "g1_1", "comparison": "in", "value": ["0", "20"]},  {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["0", "20"]},   {"attribute": "g2_2", "comparison": "=", "value": "B1"}],  [{"attribute": "g2_1", "comparison": "in", "value": ["21", "40"]}, {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["21", "40"]},  {"attribute": "g2_2", "comparison": "=", "value": "B1"}],  [{"attribute": "g2_1", "comparison": "in", "value": ["41", "60"]}, {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["41", "60"]},  {"attribute": "g2_2", "comparison": "=", "value": "B1"}],  [{"attribute": "g2_1", "comparison": "in", "value": ["61", "80"]}, {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["61", "80"]},  {"attribute": "g2_2", "comparison": "=", "value": "B1"}],  [{"attribute": "g2_1", "comparison": "in", "value": ["81", "100"]},{"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["81", "100"]}, {"attribute": "g2_2", "comparison": "=", "value": "B1"}],  [{"attribute": "g2_1", "comparison": "in", "value": ["0", "20"]},  {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                
                {"id": "c3_1", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["0", "20"]},   {"attribute": "g3_2", "comparison": "=", "value": "C1"}],  [{"attribute": "g3_1", "comparison": "in", "value": ["21", "40"]}, {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["21", "40"]},  {"attribute": "g3_2", "comparison": "=", "value": "C1"}],  [{"attribute": "g3_1", "comparison": "in", "value": ["41", "60"]}, {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["41", "60"]},  {"attribute": "g3_2", "comparison": "=", "value": "C1"}],  [{"attribute": "g3_1", "comparison": "in", "value": ["61", "80"]}, {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["61", "80"]},  {"attribute": "g3_2", "comparison": "=", "value": "C1"}],  [{"attribute": "g3_1", "comparison": "in", "value": ["81", "100"]},{"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["81", "100"]}, {"attribute": "g3_2", "comparison": "=", "value": "C1"}],  [{"attribute": "g3_1", "comparison": "in", "value": ["0", "20"]},  {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g1_2", "type": "discrete", "values": [{"key": "A1", "value": 0.5}, {"key": "A2", "value": 0.5}]}
                ]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g2_2", "type": "discrete", "values": [{"key": "B1", "value": 0.5}, {"key": "B2", "value": 0.5}]}
                ]},

            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g3_2", "type": "discrete", "values": [{"key": "C1", "value": 0.5}, {"key": "C2", "value": 0.5}]}
                ]}
        ],
    },

    "hybrid_20_complex_conditions_2_and_for_2_or": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["0", "16"]},   {"attribute": "g1_2", "comparison": "=", "value": "A1"}],  [{"attribute": "g1_1", "comparison": "in", "value": ["21", "36"]}, {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["21", "36"]},  {"attribute": "g1_2", "comparison": "=", "value": "A1"}],  [{"attribute": "g1_1", "comparison": "in", "value": ["41", "56"]}, {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["41", "56"]},  {"attribute": "g1_2", "comparison": "=", "value": "A1"}],  [{"attribute": "g1_1", "comparison": "in", "value": ["61", "76"]}, {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["61", "76"]},  {"attribute": "g1_2", "comparison": "=", "value": "A1"}],  [{"attribute": "g1_1", "comparison": "in", "value": ["81", "96"]},{"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1_1", "comparison": "in", "value": ["81", "96"]}, {"attribute": "g1_2", "comparison": "=", "value": "A1"}],  [{"attribute": "g1_1", "comparison": "in", "value": ["0", "16"]},  {"attribute": "g1_2", "comparison": "=", "value": "A2"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["0", "16"]},   {"attribute": "g2_2", "comparison": "=", "value": "B1"}],  [{"attribute": "g2_1", "comparison": "in", "value": ["21", "36"]}, {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["21", "36"]},  {"attribute": "g2_2", "comparison": "=", "value": "B1"}],  [{"attribute": "g2_1", "comparison": "in", "value": ["41", "56"]}, {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["41", "56"]},  {"attribute": "g2_2", "comparison": "=", "value": "B1"}],  [{"attribute": "g2_1", "comparison": "in", "value": ["61", "76"]}, {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["61", "76"]},  {"attribute": "g2_2", "comparison": "=", "value": "B1"}],  [{"attribute": "g2_1", "comparison": "in", "value": ["81", "96"]},{"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2_1", "comparison": "in", "value": ["81", "96"]}, {"attribute": "g2_2", "comparison": "=", "value": "B1"}],  [{"attribute": "g2_1", "comparison": "in", "value": ["0", "16"]},  {"attribute": "g2_2", "comparison": "=", "value": "B2"}]]},
                
                {"id": "c3_1", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["0", "16"]},   {"attribute": "g3_2", "comparison": "=", "value": "C1"}],  [{"attribute": "g3_1", "comparison": "in", "value": ["21", "36"]}, {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["21", "36"]},  {"attribute": "g3_2", "comparison": "=", "value": "C1"}],  [{"attribute": "g3_1", "comparison": "in", "value": ["41", "56"]}, {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["41", "56"]},  {"attribute": "g3_2", "comparison": "=", "value": "C1"}],  [{"attribute": "g3_1", "comparison": "in", "value": ["61", "76"]}, {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["61", "76"]},  {"attribute": "g3_2", "comparison": "=", "value": "C1"}],  [{"attribute": "g3_1", "comparison": "in", "value": ["81", "96"]},{"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3_1", "comparison": "in", "value": ["81", "96"]}, {"attribute": "g3_2", "comparison": "=", "value": "C1"}],  [{"attribute": "g3_1", "comparison": "in", "value": ["0", "16"]},  {"attribute": "g3_2", "comparison": "=", "value": "C2"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g1_2", "type": "discrete", "values": [{"key": "A1", "value": 0.4}, {"key": "A2", "value": 0.4}, {"key": "X", "value": 0.2}]}
                ]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g2_2", "type": "discrete", "values": [{"key": "B1", "value": 0.4}, {"key": "B2", "value": 0.4}, {"key": "Y", "value": 0.2}]}
                ]},

            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3_1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}},
                { "name": "g3_2", "type": "discrete", "values": [{"key": "C1", "value": 0.4}, {"key": "C2", "value": 0.4}, {"key": "Z", "value": 0.2}]}
                ]}
        ],
    },

}

modifications_or = {
    "pure_discrete_equal": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A5"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B4"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B5"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C4"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 0.2}, 
                                                                          {"key": "A2", "value": 0.2},
                                                                          {"key": "A3", "value": 0.2},
                                                                          {"key": "A4", "value": 0.2},
                                                                          {"key": "A5", "value": 0.2}]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0.2}, 
                                                                          {"key": "B2", "value": 0.2},
                                                                          {"key": "B3", "value": 0.2},
                                                                          {"key": "B4", "value": 0.2},
                                                                          {"key": "B5", "value": 0.2}]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0.2}, 
                                                                          {"key": "C2", "value": 0.2},
                                                                          {"key": "C3", "value": 0.2},
                                                                          {"key": "C4", "value": 0.2},
                                                                          {"key": "C5", "value": 0.2}]}]},    
        ]
    },

    "pure_discrete_equal_2": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}], [{"attribute": "g1", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A2"}], [{"attribute": "g1", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A3"}], [{"attribute": "g1", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A4"}], [{"attribute": "g1", "comparison": "=", "value": "A5"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A5"}], [{"attribute": "g1", "comparison": "=", "value": "A1"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B1"}], [{"attribute": "g1", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B2"}], [{"attribute": "g1", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}], [{"attribute": "g1", "comparison": "=", "value": "B4"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B4"}], [{"attribute": "g1", "comparison": "=", "value": "B5"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B5"}], [{"attribute": "g1", "comparison": "=", "value": "B1"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C1"}], [{"attribute": "g1", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C2"}], [{"attribute": "g1", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C3"}], [{"attribute": "g1", "comparison": "=", "value": "C4"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C4"}], [{"attribute": "g1", "comparison": "=", "value": "C5"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}], [{"attribute": "g1", "comparison": "=", "value": "C1"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 0.2}, 
                                                                          {"key": "A2", "value": 0.2},
                                                                          {"key": "A3", "value": 0.2},
                                                                          {"key": "A4", "value": 0.2},
                                                                          {"key": "A5", "value": 0.2}]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0.2}, 
                                                                          {"key": "B2", "value": 0.2},
                                                                          {"key": "B3", "value": 0.2},
                                                                          {"key": "B4", "value": 0.2},
                                                                          {"key": "B5", "value": 0.2}]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0.2}, 
                                                                          {"key": "C2", "value": 0.2},
                                                                          {"key": "C3", "value": 0.2},
                                                                          {"key": "C4", "value": 0.2},
                                                                          {"key": "C5", "value": 0.2}]}]},    
        ]
    },

    "pure_discrete_equal_5": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}], [{"attribute": "g1", "comparison": "=", "value": "A2"}], [{"attribute": "g1", "comparison": "=", "value": "A3"}], [{"attribute": "g1", "comparison": "=", "value": "A4"}], [{"attribute": "g1", "comparison": "=", "value": "A5"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A2"}], [{"attribute": "g1", "comparison": "=", "value": "A3"}], [{"attribute": "g1", "comparison": "=", "value": "A4"}], [{"attribute": "g1", "comparison": "=", "value": "A5"}], [{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A3"}], [{"attribute": "g1", "comparison": "=", "value": "A4"}], [{"attribute": "g1", "comparison": "=", "value": "A5"}], [{"attribute": "g1", "comparison": "=", "value": "A1"}], [{"attribute": "g1", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A4"}], [{"attribute": "g1", "comparison": "=", "value": "A5"}], [{"attribute": "g1", "comparison": "=", "value": "A1"}], [{"attribute": "g1", "comparison": "=", "value": "A2"}], [{"attribute": "g1", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A5"}], [{"attribute": "g1", "comparison": "=", "value": "A1"}], [{"attribute": "g1", "comparison": "=", "value": "A2"}], [{"attribute": "g1", "comparison": "=", "value": "A3"}], [{"attribute": "g1", "comparison": "=", "value": "A4"}]]},
                
                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B1"}], [{"attribute": "g2", "comparison": "=", "value": "B2"}], [{"attribute": "g2", "comparison": "=", "value": "B3"}], [{"attribute": "g2", "comparison": "=", "value": "B4"}], [{"attribute": "g2", "comparison": "=", "value": "B5"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B2"}], [{"attribute": "g2", "comparison": "=", "value": "B3"}], [{"attribute": "g2", "comparison": "=", "value": "B4"}], [{"attribute": "g2", "comparison": "=", "value": "B5"}], [{"attribute": "g2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}], [{"attribute": "g2", "comparison": "=", "value": "B4"}], [{"attribute": "g2", "comparison": "=", "value": "B5"}], [{"attribute": "g2", "comparison": "=", "value": "B1"}], [{"attribute": "g2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B4"}], [{"attribute": "g2", "comparison": "=", "value": "B5"}], [{"attribute": "g2", "comparison": "=", "value": "B1"}], [{"attribute": "g2", "comparison": "=", "value": "B2"}], [{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B5"}], [{"attribute": "g2", "comparison": "=", "value": "B1"}], [{"attribute": "g2", "comparison": "=", "value": "B2"}], [{"attribute": "g2", "comparison": "=", "value": "B3"}], [{"attribute": "g2", "comparison": "=", "value": "B4"}]]},
                

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C1"}], [{"attribute": "g3", "comparison": "=", "value": "C2"}], [{"attribute": "g3", "comparison": "=", "value": "C3"}], [{"attribute": "g3", "comparison": "=", "value": "C4"}], [{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C2"}], [{"attribute": "g3", "comparison": "=", "value": "C3"}], [{"attribute": "g3", "comparison": "=", "value": "C4"}], [{"attribute": "g3", "comparison": "=", "value": "C5"}], [{"attribute": "g3", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C3"}], [{"attribute": "g3", "comparison": "=", "value": "C4"}], [{"attribute": "g3", "comparison": "=", "value": "C5"}], [{"attribute": "g3", "comparison": "=", "value": "C1"}], [{"attribute": "g3", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C4"}], [{"attribute": "g3", "comparison": "=", "value": "C5"}], [{"attribute": "g3", "comparison": "=", "value": "C1"}], [{"attribute": "g3", "comparison": "=", "value": "C2"}], [{"attribute": "g3", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}], [{"attribute": "g3", "comparison": "=", "value": "C1"}], [{"attribute": "g3", "comparison": "=", "value": "C2"}], [{"attribute": "g3", "comparison": "=", "value": "C3"}], [{"attribute": "g3", "comparison": "=", "value": "C4"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 0.2}, 
                                                                          {"key": "A2", "value": 0.2},
                                                                          {"key": "A3", "value": 0.2},
                                                                          {"key": "A4", "value": 0.2},
                                                                          {"key": "A5", "value": 0.2}]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0.2}, 
                                                                          {"key": "B2", "value": 0.2},
                                                                          {"key": "B3", "value": 0.2},
                                                                          {"key": "B4", "value": 0.2},
                                                                          {"key": "B5", "value": 0.2}]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0.2}, 
                                                                          {"key": "C2", "value": 0.2},
                                                                          {"key": "C3", "value": 0.2},
                                                                          {"key": "C4", "value": 0.2},
                                                                          {"key": "C5", "value": 0.2}]}]},    
        ]
    },

    "hybrid_20_discrete_equal": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A5"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B4"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B5"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C4"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 0.16}, 
                                                                          {"key": "A2", "value": 0.16},
                                                                          {"key": "A3", "value": 0.16},
                                                                          {"key": "A4", "value": 0.16},
                                                                          {"key": "A5", "value": 0.16}, 
                                                                          {"key": "X", "value": 0.2}]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0.16}, 
                                                                          {"key": "B2", "value": 0.16},
                                                                          {"key": "B3", "value": 0.16},
                                                                          {"key": "B4", "value": 0.16},
                                                                          {"key": "B5", "value": 0.16},
                                                                          {"key": "Y", "value": 0.2}]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0.16}, 
                                                                          {"key": "C2", "value": 0.16},
                                                                          {"key": "C3", "value": 0.16},
                                                                          {"key": "C4", "value": 0.16},
                                                                          {"key": "C5", "value": 0.16},
                                                                          {"key": "Z", "value": 0.2}]}]},    
        ]
    },

    "pure_discrete_unbalanced": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A5"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B4"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B5"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C4"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 1}, 
                                                                          {"key": "A2", "value": 0},
                                                                          {"key": "A3", "value": 0},
                                                                          {"key": "A4", "value": 0},
                                                                          {"key": "A5", "value": 0}
                                                                          ]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0}, 
                                                                          {"key": "B2", "value": 0},
                                                                          {"key": "B3", "value": 1},
                                                                          {"key": "B4", "value": 0},
                                                                          {"key": "B5", "value": 0}
                                                                          ]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0}, 
                                                                          {"key": "C2", "value": 0},
                                                                          {"key": "C3", "value": 0},
                                                                          {"key": "C4", "value": 0},
                                                                          {"key": "C5", "value": 1}
                                                                          ]}]},    
        ]
    },

        "pure_discrete_unbalanced_2": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A5"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B5"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 1}, 
                                                                          {"key": "A2", "value": 0},
                                                                          {"key": "A3", "value": 0},
                                                                          {"key": "A4", "value": 0},
                                                                          {"key": "A5", "value": 0}
                                                                          ]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0}, 
                                                                          {"key": "B2", "value": 0},
                                                                          {"key": "B3", "value": 1},
                                                                          {"key": "B4", "value": 0},
                                                                          {"key": "B5", "value": 0}
                                                                          ]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0}, 
                                                                          {"key": "C2", "value": 0},
                                                                          {"key": "C3", "value": 0},
                                                                          {"key": "C4", "value": 0},
                                                                          {"key": "C5", "value": 1}
                                                                          ]}]},    
        ]
    },

        "pure_discrete_unbalanced_5": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 1}, 
                                                                          {"key": "A2", "value": 0},
                                                                          {"key": "A3", "value": 0},
                                                                          {"key": "A4", "value": 0},
                                                                          {"key": "A5", "value": 0}
                                                                          ]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0}, 
                                                                          {"key": "B2", "value": 0},
                                                                          {"key": "B3", "value": 1},
                                                                          {"key": "B4", "value": 0},
                                                                          {"key": "B5", "value": 0}
                                                                          ]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0}, 
                                                                          {"key": "C2", "value": 0},
                                                                          {"key": "C3", "value": 0},
                                                                          {"key": "C4", "value": 0},
                                                                          {"key": "C5", "value": 1}
                                                                          ]}]},    
        ]
    },

    "hybrid_20_discrete_unbalanced": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A1"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A2"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A3"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A4"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "=", "value": "A5"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B1"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B2"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B3"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B4"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "=", "value": "B5"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C1"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C2"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C3"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C4"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "=", "value": "C5"}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "discrete", "values": [{"key": "A1", "value": 0.8}, 
                                                                          {"key": "A2", "value": 0},
                                                                          {"key": "A3", "value": 0},
                                                                          {"key": "A4", "value": 0},
                                                                          {"key": "A5", "value": 0},
                                                                          {"key": "X", "value": 0.2}
                                                                          ]}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "discrete", "values": [{"key": "B1", "value": 0}, 
                                                                          {"key": "B2", "value": 0},
                                                                          {"key": "B3", "value": 0.8},
                                                                          {"key": "B4", "value": 0},
                                                                          {"key": "B5", "value": 0},
                                                                          {"key": "Y", "value": 0.2}
                                                                          ]}]},            
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "discrete", "values": [{"key": "C1", "value": 0}, 
                                                                          {"key": "C2", "value": 0},
                                                                          {"key": "C3", "value": 0},
                                                                          {"key": "C4", "value": 0},
                                                                          {"key": "C5", "value": 0.8},
                                                                          {"key": "Z", "value": 0.2}
                                                                          ]}]},    
        ]
    },

    "pure_continuous_values_norm": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["81", "100"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
        ]
    },

    "pure_continuous_values_norm_2": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "30"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["21", "50"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["41", "70"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["61", "90"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "30"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["21", "50"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["41", "70"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["61", "90"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "30"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["21", "50"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["41", "70"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["61", "90"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["81", "100"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
        ]
    },

    "pure_continuous_values_norm_5": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "100"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "100"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "100"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
        ]
    },

    "hybrid_20_continuous_values_norm": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "16"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["21", "36"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["41", "56"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["61", "76"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["81", "96"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "16"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["21", "36"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["41", "56"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["61", "76"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["81", "96"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "16"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["21", "36"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["41", "56"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["61", "76"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["81", "96"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
        ]
    },

    "pure_continuous_values_exp": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "20"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["21", "40"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["41", "60"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["61", "80"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["81", "100"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]}
        ]
    },

    "pure_continuous_values_exp_2": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "30"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["21", "50"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["41", "70"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["61", "90"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "30"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["21", "50"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["41", "70"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["61", "90"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["81", "100"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "30"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["21", "50"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["41", "70"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["61", "90"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["81", "100"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]}
        ]
    },

    "pure_continuous_values_exp_5": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "100"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "100"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "100"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "100"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]}
        ]
    },

    "hybrid_20_continuous_values_exp": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["0", "16"]}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["21", "36"]}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["41", "56"]}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["61", "76"]}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": "in", "value": ["81", "96"]}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["0", "16"]}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["21", "36"]}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["41", "56"]}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["61", "76"]}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": "in", "value": ["81", "96"]}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["0", "16"]}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["21", "36"]}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["41", "56"]}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["61", "76"]}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": "in", "value": ["81", "96"]}]]},
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [{ "name": "g1", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [{ "name": "g2", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [{ "name": "g3", "type": "continuous", "values": {"distribution_name": "expon", "distribution_params": [{"value": 50}, {"value": 0}, {"value": 100}]}}]}
        ]
    },


    "pure_complex_conditions_2_and": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": ">", "value": "0"}, {"attribute": "g1", "comparison": "<=", "value": "20"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": ">", "value": "20"}, {"attribute": "g1", "comparison": "<=", "value": "40"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": ">", "value": "40"}, {"attribute": "g1", "comparison": "<=", "value": "60"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": ">", "value": "60"}, {"attribute": "g1", "comparison": "<=", "value": "80"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": ">", "value": "80"}, {"attribute": "g1", "comparison": "<=", "value": "100"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": ">", "value": "0"}, {"attribute": "g2", "comparison": "<=", "value": "20"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": ">", "value": "20"}, {"attribute": "g2", "comparison": "<=", "value": "40"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": ">", "value": "40"}, {"attribute": "g2", "comparison": "<=", "value": "60"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": ">", "value": "60"}, {"attribute": "g2", "comparison": "<=", "value": "80"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": ">", "value": "80"}, {"attribute": "g2", "comparison": "<=", "value": "100"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": ">", "value": "0"}, {"attribute": "g3", "comparison": "<=", "value": "20"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": ">", "value": "20"}, {"attribute": "g3", "comparison": "<=", "value": "40"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": ">", "value": "40"}, {"attribute": "g3", "comparison": "<=", "value": "60"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": ">", "value": "60"}, {"attribute": "g3", "comparison": "<=", "value": "80"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": ">", "value": "80"}, {"attribute": "g3", "comparison": "<=", "value": "100"}]]}
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]}
        ],
    },

    "pure_complex_conditions_2_and_2": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": ">", "value": "0"}, {"attribute": "g1", "comparison": "<=", "value": "30"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": ">", "value": "20"}, {"attribute": "g1", "comparison": "<=", "value": "50"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": ">", "value": "40"}, {"attribute": "g1", "comparison": "<=", "value": "70"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": ">", "value": "60"}, {"attribute": "g1", "comparison": "<=", "value": "90"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": ">", "value": "80"}, {"attribute": "g1", "comparison": "<=", "value": "100"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": ">", "value": "0"}, {"attribute": "g2", "comparison": "<=", "value": "30"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": ">", "value": "20"}, {"attribute": "g2", "comparison": "<=", "value": "50"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": ">", "value": "40"}, {"attribute": "g2", "comparison": "<=", "value": "70"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": ">", "value": "60"}, {"attribute": "g2", "comparison": "<=", "value": "90"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": ">", "value": "80"}, {"attribute": "g2", "comparison": "<=", "value": "100"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": ">", "value": "0"}, {"attribute": "g3", "comparison": "<=", "value": "30"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": ">", "value": "20"}, {"attribute": "g3", "comparison": "<=", "value": "50"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": ">", "value": "40"}, {"attribute": "g3", "comparison": "<=", "value": "70"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": ">", "value": "60"}, {"attribute": "g3", "comparison": "<=", "value": "90"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": ">", "value": "80"}, {"attribute": "g3", "comparison": "<=", "value": "100"}]]}
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]}
        ],
    },

    "pure_complex_conditions_2_and_5": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": ">", "value": "0"}, {"attribute": "g1", "comparison": "<=", "value": "100"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": ">", "value": "0"}, {"attribute": "g1", "comparison": "<=", "value": "100"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": ">", "value": "0"}, {"attribute": "g1", "comparison": "<=", "value": "100"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": ">", "value": "0"}, {"attribute": "g1", "comparison": "<=", "value": "100"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": ">", "value": "0"}, {"attribute": "g1", "comparison": "<=", "value": "100"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": ">", "value": "0"}, {"attribute": "g2", "comparison": "<=", "value": "100"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": ">", "value": "0"}, {"attribute": "g2", "comparison": "<=", "value": "100"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": ">", "value": "0"}, {"attribute": "g2", "comparison": "<=", "value": "100"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": ">", "value": "0"}, {"attribute": "g2", "comparison": "<=", "value": "100"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": ">", "value": "0"}, {"attribute": "g2", "comparison": "<=", "value": "100"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": ">", "value": "0"}, {"attribute": "g3", "comparison": "<=", "value": "100"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": ">", "value": "0"}, {"attribute": "g3", "comparison": "<=", "value": "100"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": ">", "value": "0"}, {"attribute": "g3", "comparison": "<=", "value": "100"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": ">", "value": "0"}, {"attribute": "g3", "comparison": "<=", "value": "100"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": ">", "value": "0"}, {"attribute": "g3", "comparison": "<=", "value": "100"}]]}
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]}
        ],
    },

    "hybrid_20_complex_conditions_2_and": {
        "branch_rules": [
                {"id": "c1_1", "rules": [[{"attribute": "g1", "comparison": ">", "value": "0"}, {"attribute": "g1", "comparison": "<=", "value": "16"}]]},
                {"id": "c1_2", "rules": [[{"attribute": "g1", "comparison": ">", "value": "20"}, {"attribute": "g1", "comparison": "<=", "value": "36"}]]},
                {"id": "c1_3", "rules": [[{"attribute": "g1", "comparison": ">", "value": "40"}, {"attribute": "g1", "comparison": "<=", "value": "56"}]]},
                {"id": "c1_4", "rules": [[{"attribute": "g1", "comparison": ">", "value": "60"}, {"attribute": "g1", "comparison": "<=", "value": "76"}]]},
                {"id": "c1_5", "rules": [[{"attribute": "g1", "comparison": ">", "value": "80"}, {"attribute": "g1", "comparison": "<=", "value": "96"}]]},

                {"id": "c2_1", "rules": [[{"attribute": "g2", "comparison": ">", "value": "0"}, {"attribute": "g2", "comparison": "<=", "value": "16"}]]},
                {"id": "c2_2", "rules": [[{"attribute": "g2", "comparison": ">", "value": "20"}, {"attribute": "g2", "comparison": "<=", "value": "36"}]]},
                {"id": "c2_3", "rules": [[{"attribute": "g2", "comparison": ">", "value": "40"}, {"attribute": "g2", "comparison": "<=", "value": "56"}]]},
                {"id": "c2_4", "rules": [[{"attribute": "g2", "comparison": ">", "value": "60"}, {"attribute": "g2", "comparison": "<=", "value": "76"}]]},
                {"id": "c2_5", "rules": [[{"attribute": "g2", "comparison": ">", "value": "80"}, {"attribute": "g2", "comparison": "<=", "value": "96"}]]},

                {"id": "c3_1", "rules": [[{"attribute": "g3", "comparison": ">", "value": "0"}, {"attribute": "g3", "comparison": "<=", "value": "16"}]]},
                {"id": "c3_2", "rules": [[{"attribute": "g3", "comparison": ">", "value": "20"}, {"attribute": "g3", "comparison": "<=", "value": "36"}]]},
                {"id": "c3_3", "rules": [[{"attribute": "g3", "comparison": ">", "value": "40"}, {"attribute": "g3", "comparison": "<=", "value": "56"}]]},
                {"id": "c3_4", "rules": [[{"attribute": "g3", "comparison": ">", "value": "60"}, {"attribute": "g3", "comparison": "<=", "value": "76"}]]},
                {"id": "c3_5", "rules": [[{"attribute": "g3", "comparison": ">", "value": "80"}, {"attribute": "g3", "comparison": "<=", "value": "96"}]]}
        ], 
        "event_attributes": [
            {"event_id": "Activity_1otg2lt",
            "attributes": [
                { "name": "g1", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_1hf6wrk",
            "attributes": [
                { "name": "g2", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]},
            {"event_id": "Activity_07qkwcr",
            "attributes": [
                { "name": "g3", "type": "continuous", "values": {"distribution_name": "uniform", "distribution_params": [{"value": 0}, {"value": 100}]}}]}
        ],
    },

}


out_dir = "./out/branching_conditions/short_term_dependencies/"
xor_config = './assets/basic_xor_condition_config.json'
or_config = './assets/basic_or_condition_config.json'


def generate_branching_scenarios():
    n = len(modifications_xor)

    generate_configs(xor_config, modifications_xor, 'xor', 1)
    generate_configs(or_config, modifications_or, 'or', n + 1)
