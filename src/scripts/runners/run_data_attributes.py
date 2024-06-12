import os
import glob
from pix_framework.io.event_log import EventLogIDs

from src.discovery.attributes.attribute_discovery import discover_attributes
from src.scripts.generators.generate_data_attributes import generate_data_attributes

PROSIMOS_LOG_IDS = EventLogIDs(
    case="case_id",
    activity="activity",
    enabled_time="enable_time",
    start_time="start_time",
    end_time="end_time",
    resource="resource",
)

base_dir = './out/data_attributes/'
bpmn = 'D:/_est/PIX_discovery/ICPM/loan_application.bpmn'


def run_data_attributes():
    generate_data_attributes()

    pattern = os.path.join(base_dir, '*_*_[0-9]*.csv')
    files_to_discover = glob.glob(pattern)

    for log in files_to_discover:
        print(f"\n\n\n\n\nDISCOVERING {log}")
        discover_attributes(bpmn, log, metrics_folder=base_dir, log_ids=PROSIMOS_LOG_IDS)

    case_log = base_dir+"case_attributes.csv"
    print(f"\n\n\n\n\nDISCOVERING {case_log}")
    discover_attributes(bpmn, case_log, metrics_folder=base_dir, log_ids=PROSIMOS_LOG_IDS)


