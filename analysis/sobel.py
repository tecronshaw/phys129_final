import numpy as np
from analysis.helpers.convolve import apply_filter


def run(image_data):
    """
    Applies a Sobel filter across an image. This is essentially moving a small matrix across every pixel in the image
    and calculating the gradient of the pixel's neighbors. The returned value is an image of the same size where
    each pixel value represents that gradient value (averaged for each color channel... e.g. R, G, B).
    :return:
    """
    horizontal_kernel = np.array([[1, 0, -1],
                                  [1, 0, -1],
                                  [1, 0, -1]])

    vertical_kernel = np.array([[-1, -1, -1],
                                [0, 0, 0],
                                [1, 1, 1]])

    analyzed_image = np.zeros(image_data.shape, dtype=image_data.dtype)
    for color in range(image_data.shape[2]):
        horizontal_image = apply_filter(image_data[:, :, color], horizontal_kernel)
        vertical_image = apply_filter(image_data[:, :, color], vertical_kernel)
        distance = np.sqrt(horizontal_image ** 2 + vertical_image ** 2, dtype=np.float)
        analyzed_image[:, :, color] = distance / np.max(distance) * 255

    return analyzed_image
