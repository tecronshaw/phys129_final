import sys
from analysis import algorithm_list, run_algorithm
from matplotlib import image, pyplot as plt
from constants import IMAGE_PATH


help_text = """
Run with `python client.py <algorithm_name>`.

This script allows you to interact with a simple Pi web server. It tells the Pi to take an image,
downloads the image, and then runs the algorithm specified by <algorithm_name>.

The following algorithms are supported:

{}
""".format("\n".join(algorithm_list))


def run(algorithm_name):
    """
    Performs the following:
        - Send request to web app to capture image and download
        - Run algorithm on image based on algorithm name
        - Display result of algorithm

    :param algorithm_name:
    """
    # TODO - replace this with fetch and open
    image_data = image.imread(IMAGE_PATH)
    result = run_algorithm(algorithm_name, image_data)
    plt.imshow(result)
    plt.show()


if __name__ == '__main__':
    """
    Runs the image capture and analyze if proper arguments, else prints help text
    """
    args = sys.argv[1:]
    if len(args) > 0 and args[0] in algorithm_list:
        run(args[0])
    else:
        print(help_text)
