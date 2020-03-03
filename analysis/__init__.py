import os
import importlib


def get_algorithm_list():
    """
    :return: list of importable algorithms containing run(image_data) function
    """
    algorithms = []
    algorithm_directory = os.path.dirname(__file__)
    for filename in os.listdir(algorithm_directory):
        if filename.endswith(".py") and "__init__" not in filename:
            with open(os.path.join(algorithm_directory, filename), 'r') as f:
                if "def run(" in f.read():
                    algorithms.append(filename.replace(".py", ""))
    return algorithms


def run_algorithm(name, image_data):
    """
    Calls the run function from a module with the specified name.
    :param name:
    :param image_data: numpy array representing an image (height, width, channels)
    :return: numpy array representing the processed image (height, width, value)
    """
    print("Running {} algorithm".format(name))
    algorithm = importlib.import_module('analysis.{}'.format(name))
    return algorithm.run(image_data)


algorithm_list = get_algorithm_list()
