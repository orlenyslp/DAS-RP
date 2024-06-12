import pandas as pd
import numpy as np
import csv
import os

import random

import matplotlib
import prosimos.simulation_engine

matplotlib.use('TkAgg')  # Use the TkAgg backend (replace 'TkAgg' with another backend if needed)

import matplotlib.pyplot as plt

out_folder = "./out/data_attributes/"
bpmn = "./assets/data_attribute_model.bpmn"
config = "./assets/data_attribute_case.json"


def generate_data_attributes():
    # Global and Event Attributes
    for i in range(1, 21):
        extend_and_save_logs(i, r"./assets/data_attribute_log.csv")
    # plot_sequence()
    # Case Attributes
    prosimos.simulation_engine.run_simulation(bpmn, config, 5000, log_out_path=out_folder+"case_attributes.csv")


def extend_and_save_logs(generator_index, csv_log_path="./../assets/data/log_example.csv"):
    traces, e_traces, g_log, activities, init_activities, ev_freq = read_log(csv_log_path)
    a_id = random.choice(activities)
    while a_id in init_activities:
        a_id = random.choice(activities)

    column_headers = ["case_id", "activity", "resource", "start_time", "end_time", "data_attr"]

    ev_log_1 = generate_attr_event_log(e_traces=e_traces,
                                       update_rules_events=[a_id],
                                       generator_index=generator_index)
    save_to_csv(ev_log_1, ["case_id", "activity", "resource", "start_time", "end_time", f"se_{generator_index}"], "%ssingle_ev_attr_%d.csv" % (out_folder, generator_index))

    ev_log_n = generate_attr_event_log(e_traces=e_traces,
                                       update_rules_events=activities,
                                       generator_index=generator_index)
    save_to_csv(ev_log_n, ["case_id", "activity", "resource", "start_time", "end_time", f"me_{generator_index}"], "%smultiple_ev_attr_%d.csv" % (out_folder, generator_index))

    # Global Attributes

    glob_log_1 = genereta_attr_global_log(g_log=g_log,
                                          data_values=get_global_data_values(generator_index, ev_freq[a_id]),
                                          update_rules_events=[a_id],
                                          g_data=(0 if generator_index < 12 else None))

    save_to_csv(glob_log_1, ["case_id", "activity", "resource", "start_time", "end_time", f"sg_{generator_index}"], "%ssingle_global_attr_%d.csv" % (out_folder, generator_index))

    glob_log_n = genereta_attr_global_log(g_log=g_log,
                                          data_values=get_global_data_values(generator_index, int(len(g_log) / 2)),
                                          update_rules_events=activities,
                                          g_data=(0 if generator_index < 12 else None))
    save_to_csv(glob_log_n, ["case_id", "activity", "resource", "start_time", "end_time", f"mg_{generator_index}"], "%smultiple_global_attr_%d.csv" % (out_folder, generator_index))

    print("Generator #%d Completed" % generator_index)


def get_global_data_values(generator_index, sample_size):
    if sample_size % 2 != 0:
        sample_size += 1
    return set_up_and_call_generator(generator_index, sample_size // 2) \
           + set_up_and_call_generator(generator_index, sample_size // 2)


def save_to_csv(list_of_lists, column_headers, file_name):
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(column_headers)
        writer.writerows(list_of_lists)


def generate_attr_event_log(e_traces: dict, update_rules_events: list, generator_index):
    data_log = list()
    for c_id in e_traces:
        evts = e_traces[c_id]
        data_values = set_up_and_call_generator(generator_index, int(len(e_traces[c_id]) / 2))
        started = dict()
        g_data = 0 if generator_index < 10 else None
        i_data = 0
        for ev in evts:
            if ev['state'] == 'start':
                started[ev['index']] = [c_id, ev['activity'], ev['resource'], ev['timestamp'], None, None]
            else:
                if ev['activity'] in update_rules_events:
                    if i_data >= len(data_values):
                        print("hola")
                    g_data = data_values[i_data]
                    i_data += 1
                ev_inf = started[ev['index']]
                ev_inf[-2:] = [ev['timestamp'], g_data]
                data_log.append(ev_inf)

    return data_log


def genereta_attr_global_log(g_log: list, data_values: list, update_rules_events: list, g_data):
    i_data = 0
    data_log = list()
    started = dict()

    for ev in g_log:
        if ev['state'] == 'start':
            if ev['c_id'] not in started:
                started[ev['c_id']] = dict()
            started[ev['c_id']][ev['index']] = [ev['c_id'], ev['activity'], ev['resource'], ev['timestamp'], None, None]
        else:
            if ev['activity'] in update_rules_events:
                g_data = data_values[i_data]
                i_data += 1
            ev_inf = started[ev['c_id']][ev['index']]
            ev_inf[-2:] = [ev['timestamp'], g_data]
            data_log.append(ev_inf)
    return data_log


def read_log(csv_log_path="./../assets/data/log_example.csv"):
    log_df = pd.read_csv(csv_log_path)
    activities = log_df['activity'].unique()
    init_activities = set()

    traces = {}
    e_traces = {}
    g_log = []
    ev_freq = dict()

    for index, row in log_df.iterrows():
        case_id = row['case_id']

        if case_id not in traces:
            traces[case_id] = []
        if case_id not in e_traces:
            e_traces[case_id] = []

        traces[case_id].append(row.to_dict())
        start_event, end_event = _split_events(row, len(traces[case_id]))
        if start_event['activity'] not in ev_freq:
            ev_freq[start_event['activity']] = 0
        ev_freq[start_event['activity']] += 1

        e_traces[case_id].extend([start_event, end_event])
        g_log.extend([
            {**start_event, 'c_id': case_id},
            {**end_event, 'c_id': case_id}
        ])

    g_log.sort(key=lambda x: x['timestamp'])
    for case_id in e_traces:
        e_traces[case_id].sort(key=lambda x: x['timestamp'])
        init_activities.add(e_traces[case_id][0]['activity'])

    return traces, e_traces, g_log, activities, init_activities, ev_freq


def _split_events(row, index):
    start_event = {
        'index': index,
        'activity': row['activity'],
        'resource': row['resource'],
        'state': 'start',
        'timestamp': row['start_time']
    }
    end_event = {
        'index': index,
        'activity': row['activity'],
        'state': 'end',
        'timestamp': row['end_time']
    }
    return start_event, end_event


# -------------------- Data Generators ----------------------- #


def set_up_and_call_generator(generator_index, n_samples):
    if generator_index == 1:
        # 1. Linear Trend
        # Common in economic growth, population increases, or any phenomenon with a constant rate of change.
        # Benefits linear regression analysis due to its linear nature.
        return call_data_generator(
            'linear_trend',
            n_samples=n_samples,
            b=0.5,
            initial_value=0,
            noise_level=0.2
        )
    elif generator_index == 2:
        # Exponential Growth
        # Useful for modeling phenomena like population growth, compound interest, or infectious disease spread.
        # Challenges curve fitting and benefits from logarithmic transformation for linear regression.
        return call_data_generator(
            'exponential_growth',
            n_samples=n_samples,
            base=1.05,
            noise_level=0.2
        )
    elif generator_index == 3:
        # Lognormal Data
        # Applicable in finance (stock prices), survival analysis, and wherever data is multiplicatively affected.
        # Challenges both curve fitting and decision trees due to its skewed distribution.
        return call_data_generator(
            'lognormal_data',
            n_samples=n_samples,
            mean=0,
            sigma=0.1,
            noise_level=0.1
        )
    elif generator_index == 4:
        # AR(1) Sequence
        # Models time-series data where the next value depends linearly on its previous value plus some noise.
        # Directly challenges and benefits regression models, particularly linear and autoregressive models.

        return call_data_generator(
            'ar1',
            n_samples=n_samples,
            phi=0.8,
            noise_level=0.05
        )
    elif generator_index == 5:
        # Conditional Exponential
        # Models scenarios where growth rate changes after a certain point—useful in economics or environmental studies.
        # Challenges curve fitting, especially non-linear models.
        c_p = n_samples // 4
        return call_data_generator(
            'conditional_exponential',
            n_samples=n_samples,
            change_points=[c_p, 2 * c_p, 3 * c_p],
            growth_rates=[0.05, 0.1, 0.05, 0.1],
            base=2,
            noise_level=0.05
        )
    elif generator_index == 6:
        # Sinusoidal Sequence
        # Models oscillating phenomena like waves, seasonal sales, or circadian rhythms.
        # Challenges models to fit periodic patterns, beneficial for regression analysis with transformation.
        return call_data_generator(
            'sinusoidal',
            n_samples=n_samples,
            amplitude=1,
            frequency=0.1,
            noise_level=0.1
        )
    elif generator_index == 7:
        # Switching Regression
        # Useful in scenarios where system dynamics change over time.
        #           For example, regime changes in economics or fault detection.
        # Challenges decision trees and regression models to adapt to abrupt changes in data patterns.
        return call_data_generator(
            'switching_regression',
            n_samples=n_samples,
            models=[(0.5, 1), (-0.5, 1), (0.2, -2), (-0.1, 3)],
            noise_level=0.1
        )
    elif generator_index == 8:
        # Piecewise Linear
        # Models piecewise events like tax brackets, production rates, or energy usage efficiency at different levels.
        # Useful for regression analysis and challenges models to fit multiple linear trends within one dataset.
        return call_data_generator(
            'piecewise_linear',
            n_samples=n_samples,
            num_segments=10,
            num_repeats=1,
            noise_level=0.2
        )
    elif generator_index == 9:
        # Uniform Data
        # Simulates scenarios where every outcome within a range is equally probable, such as random drawings.
        # Tests the robustness of decision trees and regression models against uniformly distributed noise.
        return call_data_generator(
            'uniform_data',
            n_samples=n_samples,
            lower_bound=0,
            upper_bound=10,
            noise_level=0.05
        )

    elif generator_index == 10:
        # Normal Distribution
        # Generates a sequence of values based on a normal distribution with a specified mean and standard deviation, and added Gaussian noise.
        return call_data_generator(
            'normal_distribution',
            n_samples=n_samples,
            mean=500,
            std_dev=100,
            noise_level=0.05
        )
    elif generator_index == 11:
        # High Self-Transition Probability
        # Generates a sequence of categorical states with high self-transition probabilities, useful for simulating scenarios where states are likely to remain the same.
        return call_data_generator(
            'categorical_transitions',
            n_samples=n_samples,
            states=[None, "State1", "State2"],
            p_matrix=[[0.0, 0.9, 0.1], [0.0, 0.8, 0.2], [0.0, 0.7, 0.3]]
        )
    elif generator_index == 12:
        # Categorical Transitions
        # Simulates Markov chains, useful in modeling state transitions in finance, genetics, or game theory.
        # Challenges decision trees to identify and predict categorical outcomes based on transition probabilities.
        return call_data_generator(
            'categorical_transitions',
            n_samples=n_samples,
            states=[None, "State1", "State2", "State3"],
            p_matrix=[[0.0, 0.3, 0.3, 0.4], [0.0, 0.1, 0.45, 0.45], [0.0, 0.45, 0.1, 0.45], [0.0, 0.45, 0.45, 0.1]]
        )
    elif generator_index == 13:
        # Rare Transition to Specific State
        # Generates a sequence of categorical states where certain transitions to specific states are rare, useful for modeling rare events.
        return call_data_generator(
            'categorical_transitions',
            n_samples=n_samples,
            states=[None, "State1", "State2", "State3"],
            p_matrix=[[0.0, 0.4, 0.4, 0.2], [0.0, 0.5, 0.5, 0.0], [0.0, 0.4, 0.4, 0.2], [0.0, 0.4, 0.4, 0.2]]
        )
    elif generator_index == 14:
        # Uniform Transition Probabilities
        # Generates a sequence of categorical states with uniform transition probabilities, meaning each state has an equal probability of transitioning to any other state.
        return call_data_generator(
            'categorical_transitions',
            n_samples=n_samples,
            states=[None, "State1", "State2", "State2"],
            p_matrix=[[0.0, 0.33, 0.33, 0.34], [0.0, 0.33, 0.33, 0.34], [0.0, 0.33, 0.33, 0.34], [0.0, 0.33, 0.33, 0.34]]
        )
    elif generator_index == 15:
        # One State Dominates Transitions
        # Generates a sequence of categorical states where one state dominates the transitions, meaning there is a higher probability of transitioning to a specific state.
        return call_data_generator(
            'categorical_transitions',
            n_samples=n_samples,
            states=[None, "StateX", "StateY", "StateZ"],
            p_matrix=[[0.0, 0.1, 0.1, 0.8], [0.0, 0.2, 0.2, 0.6], [0.0, 0.3, 0.3, 0.4], [0.0, 0.4, 0.4, 0.2]]
        )
    elif generator_index == 16:
        # Cyclic Transitions
        # Generates a sequence of categorical states with cyclic transitions, meaning the states transition in a fixed cyclic order.
        return call_data_generator(
            'categorical_transitions',
            n_samples=n_samples,
            states=[None, "State1", "State2", "State3", "State4"],
            p_matrix=[[0.0, 0.25, 0.25, 0.25, 0.25], [0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0]]
        )
    elif generator_index == 17:
        # Random States - 2 States with Equal Probabilities
        # Generates a sequence of random states with equal probabilities of two states, useful for simulating binary outcomes.
        return call_data_generator(
            'random_states',
            n_samples=n_samples,
            states=["State1", "State2"],
            probabilities=[0.5, 0.5]
        )
    elif generator_index == 18:
        # Random States - 2 States with Non-Equal Probabilities
        # Generates a sequence of random states with non-equal probabilities of two states, useful for simulating biased binary outcomes.
        return call_data_generator(
            'random_states',
            n_samples=n_samples,
            states=["State1", "State2"],
            probabilities=[0.8, 0.2]
        )
    elif generator_index == 19:
        # Random States - 5 States with Equal Probabilities
        # Generates a sequence of random states with equal probabilities of five states, useful for simulating scenarios with multiple equally likely outcomes.
        return call_data_generator(
            'random_states',
            n_samples=n_samples,
            states=["State1", "State2", "State3", "State4", "State5"],
            probabilities=[0.2, 0.2, 0.2, 0.2, 0.2]
        )
    elif generator_index == 20:
        # Random States - 5 States with Non-Equal Probabilities
        # Generates a sequence of random states with non-equal probabilities of five states, useful for simulating scenarios with multiple outcomes with different likelihoods.
        return call_data_generator(
            'random_states',
            n_samples=n_samples,
            states=["State1", "State2", "State3", "State4", "State5"],
            probabilities=[0.1, 0.15, 0.2, 0.25, 0.3]
        )
    return []


def plot_sequence(n_samples=2000):
    # Example sequence of numbers
    sequence = get_global_data_values(10, n_samples)

    midpoint = len(sequence) // 2

    train = sequence[:midpoint]
    test = sequence[midpoint:]

    # Create two subplots side by side
    fig, axs = plt.subplots(1, 2)

    # Plot list1 on the first subplot
    axs[0].plot(train)
    axs[0].set_title('Train')

    # Plot list2 on the second subplot
    axs[1].plot(test)
    axs[1].set_title('Test')

    # Show the plot
    plt.show()


def generate_linear_trend(n_samples, b, initial_value, noise_level=0.05):
    """
    Generates a sequence of values where each value is a linear transformation of the previous value,
    with added Gaussian noise.

    Parameters:
    - n_samples (int): Total number of values in the sequence.
    - a (float): Multiplier (similar to slope in linear regression) in the recursive relation.
    - b (float): Constant term (similar to intercept in linear regression).
    - initial_value (float): Starting value for the sequence.
    - noise_level (float): Standard deviation of Gaussian noise added to each value.

    Returns:
    - np.array: Generated sequence of values.
    """

    values = np.zeros(n_samples)

    values[0] = initial_value + np.random.normal(scale=noise_level)

    for i in range(1, n_samples):
        values[i] = values[i - 1] + b + np.random.normal(scale=noise_level)  # Apply recursive formula with noise

    return values.tolist()


def generate_exponential_growth(n_samples, base, noise_level=0.1):
    """
    Generates a sequence of values following an exponential growth pattern,
    with each value adjusted by Gaussian noise.

    Parameters:
    - n_samples (int): Total number of values in the sequence.
    - base (float): The base of the exponential function, representing the growth rate.
    - noise_level (float): Standard deviation of Gaussian noise added to each value.

    Returns:
    - np.array: Generated sequence of exponential growth values.
    """
    # Generate values exponentially
    n_samples = n_samples
    return (base ** np.arange(n_samples) + np.random.normal(scale=noise_level, size=n_samples)).tolist()


def generate_sinusoidal_sequence(n_samples, amplitude, frequency, noise_level=0.1):
    """
    Generates a sequence of sinusoidal values with added Gaussian noise.

    Parameters:
    - n_samples (int): Total number of values in the sequence.
    - amplitude (float): Amplitude of the sinusoidal wave.
    - frequency (float): Frequency of the sinusoidal wave.
    - noise_level (float): Standard deviation of Gaussian noise added to each value.

    Returns:
    - np.array: Sequence of sinusoidal values.
    """
    # Generate the x values
    x = np.arange(n_samples)
    # Compute the sinusoidal values
    values = amplitude * np.sin(2 * np.pi * frequency * x) + np.random.normal(scale=noise_level, size=n_samples)
    return values.tolist()


def generate_ar1_sequence(n_samples, phi, noise_level=0.1):
    """
    Generates a sequence of values following an AR(1) model with added Gaussian noise.

    Parameters:
    - n_samples (int): Total number of values in the sequence.
    - phi (float): The coefficient of the AR(1) model, indicating the dependence on the previous value.
    - noise_level (float): Standard deviation of Gaussian noise added to each value.

    Returns:
    - np.array: Generated sequence of AR(1) values.
    """
    x = np.zeros(n_samples)
    x[0] = np.random.normal(scale=noise_level)  # Initialize the first value with noise

    # Generate the AR(1) values
    for i in range(1, n_samples):
        x[i] = phi * x[i - 1] + np.random.normal(scale=noise_level)

    return x.tolist()


def generate_categorical_transitions(n_samples, states, p_matrix):
    """
        Generates a sequence of categorical states based on specified transition probabilities,
        simulating a Markov chain process.

        Parameters:
        - n_samples (int): The number of samples (transitions) to generate in the sequence.
        - states (list): A list of possible states in the Markov chain. Each state must be unique.
        - p_matrix (list of lists): A transition probability matrix where `p_matrix[i][j]` represents
          the probability of transitioning from state `i` to state `j`. Each sub-list should sum to 1.

        Returns:
        - list: A list containing the sequence of states generated by the Markov process.
    """
    current_state = None
    categorical = []

    for _ in range(0, n_samples):
        current_state_index = states.index(current_state)
        current_state = np.random.choice(states, p=p_matrix[current_state_index])
        categorical.append(current_state)

    return categorical


def generate_piecewise_linear_sequence(n_samples, num_segments, num_repeats, noise_level=0.05):
    """
    Generates a periodic sequence of values following a piecewise linear function with added Gaussian noise,
    ensuring that each repetition of the sequence has unique noise characteristics.

    Parameters:
    - n_samples (int): Total number of values in the sequence.
    - num_segments (int): Number of segments to create in the sequence.
    - num_repeats (int): Number of times the sequence repeats.
    - noise_level (float): Standard deviation of Gaussian noise added to each value.

    Returns:
    - np.array: Generated periodic sequence of piecewise linear values with unique noise per repetition.
    """
    # Calculate the total number of samples in a single sequence before repeating
    sequence_length = n_samples // num_repeats
    segment_length = sequence_length // num_segments

    # Generate slopes and intercepts for each segment
    slopes = np.linspace(-1, 1, num_segments) * (-1) ** np.arange(num_segments)
    intercepts = np.linspace(-10, 10, num_segments)

    # Initialize an array to hold all sequences
    all_sequences = np.zeros(n_samples)

    for repeat in range(num_repeats):
        # Initialize an array for the single sequence in this repeat
        single_sequence = np.zeros(sequence_length)

        for i in range(num_segments):
            start = i * segment_length
            # Ensure the last segment fills the remaining part of the sequence
            end = start + segment_length if (i < num_segments - 1) else sequence_length
            x_segment = np.arange(start, end)

            # Add unique noise for each repeat of the sequence
            single_sequence[start:end] = slopes[i] * x_segment + intercepts[i] + np.random.normal(scale=noise_level,
                                                                                                  size=(end - start))

        # Place the repeated sequence with unique noise into the total sequence array
        all_sequences[repeat * sequence_length:(repeat + 1) * sequence_length] = single_sequence

    return all_sequences.tolist()


def generate_switching_regression_sequence(n_samples, models, noise_level=0.05):
    """
    Generates a sequence of values following a switching regression model with transitions
    distributed to be representative in both the training and testing datasets.

    Parameters:
    - n_samples (int): Total number of values in the sequence.
    - models (list of tuples): Each tuple contains (slope, intercept) for each segment.
    - noise_level (float): Standard deviation of Gaussian noise added to each value.

    Returns:
    - np.array: Generated sequence of switching regression values.
    """
    values = np.zeros(n_samples)
    num_segments = len(models)
    segment_length = n_samples // num_segments

    current_index = 0
    for i, (slope, intercept) in enumerate(models):
        # Calculate end index for the current segment
        if i == num_segments - 1:
            end_index = n_samples
        else:
            end_index = current_index + segment_length

        # Generate values for the current segment
        x_segment = np.arange(current_index, end_index)
        values[current_index:end_index] = slope * x_segment + intercept + np.random.normal(scale=noise_level, size=(
                end_index - current_index))

        # Update the starting index for the next segment
        current_index = end_index

    return values.tolist()


def generate_uniform_data_sequence(n_samples, lower_bound, upper_bound, noise_level=0.05):
    """
    Generates a sequence of values sampled from a uniform distribution within the specified bounds,
    with added Gaussian noise.

    Parameters:
    - n_samples (int): Total number of values in the sequence.
    - lower_bound (float): Lower boundary of the uniform distribution.
    - upper_bound (float): Upper boundary of the uniform distribution.
    - noise_level (float): Standard deviation of Gaussian noise added to each value.

    Returns:
    - np.array: Generated sequence of uniform values with noise.
    """
    # Generate values from a uniform distribution and add Gaussian noise
    values = np.random.uniform(lower_bound, upper_bound, n_samples) + np.random.normal(scale=noise_level,
                                                                                       size=n_samples)

    return values.tolist()


def generate_lognormal_data_sequence(n_samples, mean, sigma, noise_level=0.1):
    """
    Generates a sequence of values sampled from a lognormal distribution,
    modeled by exponential growth of a normally distributed variable, with added Gaussian noise.

    Parameters:
    - n_samples (int): Total number of values in the sequence.
    - mean (float): Mean value used in the exponentiation to create lognormal distribution.
    - sigma (float): Sigma value used in the exponentiation, affecting dispersion of the lognormal distribution.
    - noise_level (float): Standard deviation of Gaussian noise added to each value.

    Returns:
    - np.array: Generated sequence of lognormal values with noise.
    """
    # Generate an array of linearly spaced values as the base for the exponentiation
    x = np.linspace(0, 10, n_samples)
    # Generate lognormal values from exponential of a normal distribution and add Gaussian noise
    values = np.exp(mean + sigma * x) + np.random.normal(scale=noise_level, size=n_samples)

    return values.tolist()


def generate_conditional_exponential_sequence(n_samples, change_points, growth_rates, base, noise_level=0.05):
    """
    Generates a sequence of values following a conditional exponential growth model,
    with added Gaussian noise. The growth rate changes at specified change points.

    Parameters:
    - n_samples (int): Total number of values in the sequence.
    - change_points (list of int): Indices at which the growth rate changes.
    - growth_rates (list of float): The growth rates for each segment.
    - base (float): The base of the exponential function, affecting the growth rate.
    - noise_level (float): Standard deviation of Gaussian noise added to each value.

    Returns:
    - np.array: Generated sequence of exponential growth values.
    """
    if len(change_points) + 1 != len(growth_rates):
        raise ValueError("There must be one more growth rate than change points.")

    values = np.zeros(n_samples)
    current_start = 0

    # Calculate values for each segment
    for i, point in enumerate(change_points + [n_samples]):
        rate = growth_rates[i]
        end = point if i < len(change_points) else n_samples
        x_segment = np.arange(end - current_start)
        values[current_start:end] = base ** (rate * x_segment)
        current_start = end  # Update the start for the next segment

    # Add Gaussian noise to the values
    values += np.random.normal(scale=noise_level, size=n_samples)

    return values.tolist()


def generate_normal_distribution(n_samples, mean, std_dev, noise_level=0.05):
    """
    Generates a sequence of values based on a normal distribution with added Gaussian noise.

    Parameters:
    - n_samples (int): Total number of values in the sequence.
    - mean (float): Mean of the normal distribution.
    - std_dev (float): Standard deviation of the normal distribution.
    - noise_level (float): Standard deviation of Gaussian noise added to each value.

    Returns:
    - list: Generated sequence of normal distribution values.
    """
    values = np.random.normal(mean, std_dev, n_samples) + np.random.normal(scale=noise_level, size=n_samples)
    return values.tolist()


def generate_exponential_distribution(n_samples, scale, noise_level=0.05):
    """
    Generates a sequence of values based on an exponential distribution with added Gaussian noise.

    Parameters:
    - n_samples (int): Total number of values in the sequence.
    - scale (float): Scale parameter (inverse of the rate parameter) for the exponential distribution.
    - noise_level (float): Standard deviation of Gaussian noise added to each value.

    Returns:
    - list: Generated sequence of exponential distribution values.
    """
    values = np.random.exponential(scale, n_samples) + np.random.normal(scale=noise_level, size=n_samples)
    return values.tolist()


def generate_uniform_distribution(n_samples, lower_bound, upper_bound, noise_level=0.05):
    """
    Generates a sequence of values based on a uniform distribution with added Gaussian noise.

    Parameters:
    - n_samples (int): Total number of values in the sequence.
    - lower_bound (float): Lower boundary of the uniform distribution.
    - upper_bound (float): Upper boundary of the uniform distribution.
    - noise_level (float): Standard deviation of Gaussian noise added to each value.

    Returns:
    - list: Generated sequence of uniform distribution values.
    """
    values = np.random.uniform(lower_bound, upper_bound, n_samples) + np.random.normal(scale=noise_level, size=n_samples)
    return values.tolist()


def generate_random_states(n_samples, states, probabilities):
    """
    Generates a sequence of categorical states based on specified probabilities,
    without considering the previous state.

    Parameters:
    - n_samples (int): The number of samples to generate in the sequence.
    - states (list): A list of possible states. Each state must be unique.
    - probabilities (list): A list of probabilities corresponding to each state. 
      The sum of the probabilities should be 1.

    Returns:
    - list: A list containing the sequence of states generated randomly based on the specified probabilities.
    """
    return np.random.choice(states, size=n_samples, p=probabilities).tolist()




def call_data_generator(generator_id, n_samples, *args, **kwargs):
    """
    Calls one of several data generation functions based on the provided ID.

    Parameters:
    - generator_id (str): Identifier for the data generator.
    - n_samples (int): Total number of samples to generate.
    - args: Positional arguments for the data generators.
    - kwargs: Keyword arguments for the data generators.

    Returns:
    - np.array: Generated data sequence.
    """

    # Map of generator IDs to functions
    generators = {
        'linear_trend': generate_linear_trend,
        'exponential_growth': generate_exponential_growth,
        'sinusoidal': generate_sinusoidal_sequence,
        'ar1': generate_ar1_sequence,
        'categorical_transitions': generate_categorical_transitions,
        'piecewise_linear': generate_piecewise_linear_sequence,
        'switching_regression': generate_switching_regression_sequence,
        'uniform_data': generate_uniform_data_sequence,
        'lognormal_data': generate_lognormal_data_sequence,
        'conditional_exponential': generate_conditional_exponential_sequence,
        'normal_distribution': generate_normal_distribution,
        'exponential_distribution': generate_exponential_distribution,
        'uniform_distribution': generate_uniform_distribution,
        'random_states': generate_random_states
    }

    # Check if the generator ID is valid
    if generator_id in generators:
        generator_function = generators[generator_id]
        return generator_function(n_samples, *args, **kwargs)
    else:
        raise ValueError(f"No generator found for ID '{generator_id}'")


if __name__ == "__main__":
    main()
