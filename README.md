# Data-Aware Simulation Model

This repository serves as a reproducibility package, enabling the execution of experiments outlined in the research paper: "Discovery and Simulation of Data-Aware Business
Processes"

It includes the necessary source code, datasets, models, and execution guidelines, joining the four necessary systems/libraries into one repository for convenience. The extended systems referenced in the papers are [Simod](https://github.com/AutomatedProcessImprovement/Simod), [pix-framework](https://github.com/AutomatedProcessImprovement/pix-framework) and [Prosimos](https://github.com/AutomatedProcessImprovement/Prosimos), while the [log-distance-measures](https://github.com/AutomatedProcessImprovement/log-distance-measures) library provides the metrics used in the evaluation. For the most recent updates and full functionalities, please follow the provided links to access the source codes.



## Requirements
* Python 3.9
* Use [Poetry](https://python-poetry.org/)



## Required Steps

* Install the Poetry by following the instructions in the links in the Requirements subsection above.

* Clone this repository. Move to the project folder, install the dependencies by running the following command: `poetry install`

* To run the experiments consider using this commands:
  * `poetry run data-attributes` to run data attributes evaluation (synthetic logs)
  * `poerty run branching-conditions` to run branching condition evaluation (synthetic logs)
  * `poetry run real-life` to run evaluation for real life logs (BPIC2019, Sepsis and Trafic cases)




## Checking the Results

Results reported in the paper are available here [experiment_results.xlsx](experiment_results.xlsx)

### Data Attributes Results

The script first generates 20 logs for each attribute type (global and local) and for multiple or single change within the simulation + log with 10 case attributes
All logs will be saved under `out/data_attributes` folder. Then for each log it runs data attribute discovery function and appends metric results to the corresponding "metric result" file.
`metrics_continuous.csv` will contain all results for global/event attributes with numerical values, while `metrics_discrete.csv` will contain results for categorical results. `metrics_case.csv` contain both numerical and categorical results, but only for `case attributes`
Description of each generator used for branching conditions can be found here [generate_data_attributes.py](src%2Fscripts%2Fgenerators%2Fgenerate_data_attributes.py)

### Branching Condition Results

The script first generates 80 configuration files (20 for XOR with short-term dependencies and 20 with long-term dependencies), then does the same for OR gateway. Next we run simulation to create original log (giving 80 logs). Next we split original log into `train` and `test` logs, run the discovery on `train` log. Based on received results we simulate 1 log with traditional approach (without conditions) and second with `Data-Aware Simulation` model and compare received logs to `test` log. For comparison we use *N-Gram* distance (n=3) comparing the received control-flow between pairs original-traditional and original-conditional models.
Description of each generator used for branching conditions can be found here for short-term dependencies [generate_branching_conditions_short.py](src%2Fscripts%2Fgenerators%2Fgenerate_branching_conditions_short.py) and for long-term dependencies [generate_branching_conditions_long.py](src%2Fscripts%2Fgenerators%2Fgenerate_branching_conditions_long.py)
Metrics for each run will be save in a single file (long and short term dependencies separately) at `out/branching_conditions/long_term_dependencies/simulation_metrics.csv`

### Real Life Logs Results

Here we use already discovered bpmn model and configuration file with Simod (saved in assets). We split the log into `train` and `test`, discover attributes and branching conditions using `train` log, updating the copy of the discovered traditional log and insert there `Data-Aware Model` components. Then we simulate 2 logs as we did with `Branching Condition` tests.
Data attribute results will be available for each model separately under real-life log name `BPIC2019`, `Sepsis`, `Trafic` in `out/real_life` folder and split in the same way as for `Data Attribute` tests. 