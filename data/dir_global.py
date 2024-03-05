import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_FILES_PATH = os.path.join(ROOT_DIR, "data")
#ALLURE_RESULTS_PATH = os.path.join(ROOT_DIR, "allure-results")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(SCRIPT_DIR, "csv_file")
