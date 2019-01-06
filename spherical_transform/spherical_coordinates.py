import numpy as np

import sys

def cart2sph(x, y, z):
    hxy = np.hypot(x, y)
    r = np.hypot(hxy, z)
    el = np.arctan2(z, hxy)
    az = np.arctan2(y, x)
    return az, el, r


def sph2cart(az, el, r):
    rcos_theta = r * np.cos(el)
    x = rcos_theta * np.cos(az)
    y = rcos_theta * np.sin(az)
    z = r * np.sin(el)
    return x, y, z


def find_spherical_matrix_dimensions(cartesian_image_shape):
    theta = 360
    phi = 360
    hxy = np.hypot(cartesian_image_shape[0], cartesian_image_shape[1])
    r = int(np.floor(np.hypot(hxy, cartesian_image_shape[2])/2))

    return theta, phi, r


def create_spherical_matrix_from_cartesian(cartesian_image):

    cart_shape = cartesian_image.shape
    az, el, r = find_spherical_matrix_dimensions(cart_shape)

    sph_img = np.zeros((az, el, r))

    for index, value in np.ndenumerate(sph_img):
        rcos_theta = index[2] * np.cos(index[1])
        x = cart_shape[0]/2 + rcos_theta * np.cos(index[0])
        y = cart_shape[1]/2 + rcos_theta * np.sin(index[0])
        z = cart_shape[2]/2 + index[2] * np.sin(index[1])

        if 0 <= x < cart_shape[0] and 0 <= y < cart_shape[1] and 0 <= z < cart_shape[2]:

            if index[1] % 359 == 0 or index[1]  == 0:
                sys.stdout.write("\r{0} {1} {2}".format(*index))
                sys.stdout.flush()

            sph_img[index[0], index[1], index[2]] = cartesian_image[int(np.floor(x)),
                                                                    int(np.floor(y)),
                                                                    int(np.floor(z))]

    print('\nDone with creating polar image... \n Building a graph...')
    return sph_img




