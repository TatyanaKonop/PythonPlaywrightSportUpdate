from dotenv import load_dotenv
import os

# path to current file
current_file = os.path.abspath(__file__)
# name folder of project
project_folder = os.path.basename(os.path.dirname(current_file))
# absolute path to parent directory
root_dir = os.path.dirname(os.path.dirname(current_file))
# create path with the project directory
ROOT_DIR = os.path.join(root_dir, project_folder)
# create environment variable
os.environ["ROOT_DIR"] = ROOT_DIR



load_dotenv() # credentials like token, login, password download from .env or secrets
# show route fixtures
pytest_plugins = [
    'fixtures.page'
]