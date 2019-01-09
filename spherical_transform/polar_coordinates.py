import numpy as np


def find_polar_dimensions(cartesian_image_shape):
    phi = 360
    r = int(np.floor((np.hypot(cartesian_image_shape[0], cartesian_image_shape[1]))/2))

    return phi, r

def find_cartesian_dimensions(cartesian_image_shape):
    x = y = np.int(np.floor(2 * cartesian_image_shape[-1]/np.sqrt(2)))
    return x, y


def create_polar_image(cartesian_image):
    cart_shape = cartesian_image.shape
    az, r = find_polar_dimensions(cart_shape)
    print(az, r)

    polar_img = np.zeros((az, r))

    for index, value in np.ndenumerate(polar_img):
        x = cart_shape[0]/2 + index[1] * np.cos(np.deg2rad(index[0]))
        y = cart_shape[1]/2 + index[1] * np.sin(np.deg2rad(index[0]))

        if 0 <= x < cart_shape[0] - 1  and 0 <= y < cart_shape[1] - 1:
            polar_img[index[0], index[1]] = cartesian_image[int(np.round(x)), int(np.round(y))]

    return polar_img


def create_cartesian_image(polar_image):
    polar_shape = polar_image.shape
    x, y = find_cartesian_dimensions(polar_shape)
    print(x, y)

    cart_img = np.zeros((x, y))
    print(x, y)

    for index, value in np.ndenumerate(cart_img):
            center_x = index[0] - x/2
            center_y = index[1] - y/2
            r = np.sqrt(center_x**2 + center_y**2)
            phi = np.rad2deg(np.arctan2(center_x, center_y))

            cart_img[index] = polar_image[int(np.floor(phi)), int(np.floor(r))]

    return cart_img


