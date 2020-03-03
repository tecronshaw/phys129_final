from scipy.ndimage.filters import convolve


def apply_filter(image_data, kernel):
    """
    Runs a filter convolution on an image with the passed in kernel
    :param image_data:
    :param kernel:
    :return:
    """
    origin = (-int(kernel.shape[1] / 2), 0)
    return convolve(image_data, kernel, mode="reflect", origin=origin)
