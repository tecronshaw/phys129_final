import sys
from analysis import algorithm_list, run_algorithm
from matplotlib import image, pyplot as plt
from constants import CLIENT_IMAGE_PATH, IMAGE_URL
import requests


help_text = """
Run with `python client.py <algorithm_name>`.

This script allows you to interact with a simple Pi web server. It tells the Pi to take an image,
downloads the image, and then runs the algorithm specified by <algorithm_name>.

The following algorithms are supported:

{}
""".format("\n".join(algorithm_list))


def request_server_image():
    """
    Makes request to web server responsible for capturing image and returning in response
    :return:
    """
    print("Requesting image from {} for download and analysis".format(IMAGE_URL))
    r = requests.get(IMAGE_URL, allow_redirects=True)
    open(CLIENT_IMAGE_PATH, 'wb').write(r.content)
    print("Downloaded image to {}".format(CLIENT_IMAGE_PATH))
    return image.imread(CLIENT_IMAGE_PATH)


def run(algorithm_name):
    """
    Performs the following:
        - Send request to web app to capture image and download
        - Run algorithm on image based on algorithm name
        - Display result of algorithm

    :param algorithm_name:
    """
    image_data = request_server_image()
    result = run_algorithm(algorithm_name, image_data)
    fig = plt.figure()
    ax = [fig.add_subplot(1, 2, 1)]
    plt.imshow(image_data)
    ax[-1].set_title("Original")
    ax.append(fig.add_subplot(1, 2, 2))
    plt.imshow(result)
    ax[-1].set_title("With {}".format(algorithm_name))
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
