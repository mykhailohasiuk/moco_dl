import numpy as np


def find_polar_dimensions(cartesian_image_shape):
    phi = 360
    r = int(np.floor((np.hypot(cartesian_image_shape[0], cartesian_image_shape[1]))/2))

    return phi, r


def create_polar_image(cartesian_image):
    cart_shape = cartesian_image.shape
    az, r = find_polar_dimensions(cart_shape)
    print(az, r)

    polar_img = np.zeros((az, r))

    for index, value in np.ndenumerate(polar_img):
        x = cart_shape[0]/2 + index[1] * np.cos(index[0])
        y = cart_shape[1]/2 + index[1] * np.sin(index[0])

        print(x, y)

        if 0 <= x < cart_shape[0] and 0 <= y < cart_shape[1]:
            polar_img[index[0], index[1]] = cartesian_image[int(np.floor(x)), int(np.floor(y))]

    return polar_img


