import numpy as np
from analysis.helpers.convolve import apply_filter


def get_gaussian_kernel(size=15):
    """
    Generates a small gaussian matrix centered at the peak
    :param size:
    :return:
    """
    x = np.arange(-size, size, 1)
    y = np.copy(x)
    xx, yy = np.meshgrid(x, y)
    kernel = np.exp(- xx ** 2 - yy * 2)
    return kernel / kernel.sum()


def run(image_data):
    """
    Applies a Gaussian filter across an image. This essentially blurs the image.
    :return:
    """
    gaussian_kernel = get_gaussian_kernel()

    analyzed_image = np.zeros(image_data.shape, dtype=image_data.dtype)
    for color in range(image_data.shape[2]):
        analyzed_image[:, :, color] = apply_filter(image_data[:, :, color], gaussian_kernel)

    return analyzed_image
