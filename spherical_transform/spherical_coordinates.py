import numpy as np
import sys


def interp_v2(point, array):

    xmax = array.shape[0]-1
    ymax = array.shape[1]-1
    zmax = array.shape[2]-1

    eps = 1e-6

    x = point[0]
    y = point[1]
    z = point[2]

    x0 = np.int(np.floor(x))
    y0 = np.int(np.floor(y))
    z0 = np.int(np.floor(z))

    if x < xmax and y < ymax and z < zmax:

        x1 = np.int(np.ceil(x))
        y1 = np.int(np.ceil(y))
        z1 = np.int(np.ceil(z))

        xd = (x - x0) + eps / ((x1 - x0) + eps)
        yd = (y - y0) + eps / ((y1 - y0) + eps)
        zd = (z - z0) + eps / ((z1 - z0) + eps)

        c000 = array[x0, y0, z0]
        c001 = array[x0, y0, z1]
        c010 = array[x0, y1, z0]
        c011 = array[x0, y1, z1]
        c100 = array[x1, y0, z0]
        c101 = array[x1, y0, z1]
        c110 = array[x1, y1, z0]
        c111 = array[x1, y1, z1]

        c00 = (c000 * (1 - xd)) + (c100 * xd)
        c01 = (c001 * (1 - xd)) + (c101 * xd)
        c10 = (c010 * (1 - xd)) + (c110 * xd)
        c11 = (c011 * (1 - xd)) + (c111 * xd)

        c0 = (c00 * (1 - yd)) + (c10 * yd)
        c1 = (c01 * (1 - yd)) + (c11 * yd)

        c = (c0 * (1 - zd)) + (c1 * zd)

    else:
        c = array[x0, y0, z0]

    return c


def create_polar_matrix_from_cartesian(cartesian_image):

    cart_shape = cartesian_image.shape

    spherical_shape = (360, 360, np.int(np.ceil(0.5 * np.sqrt((cartesian_image.shape[0]**2)
                                                              + (cartesian_image.shape[1]**2)
                                                              + (cartesian_image.shape[2]**2)
                                                              )
                                                )
                                        )
                       )
    spherical_matrix = np.zeros(spherical_shape)

    for index, value in np.ndenumerate(spherical_matrix):
        x = index[2] * np.cos(np.deg2rad(index[0])) * np.cos(np.deg2rad(index[1])) + cart_shape[0]/2
        y = index[2] * np.cos(np.deg2rad(index[0])) * np.sin(np.deg2rad(index[1])) + cart_shape[1]/2
        z = index[2] * np.sin(np.deg2rad(index[0])) + cart_shape[-1]/2

        if 0 <= x < cart_shape[0] and 0 <= y < cart_shape[1] and 0 <= z < cart_shape[2]:
            spherical_matrix[index[0], index[1], index[2]] = interp_v2((x, y, z), cartesian_image)

            if index[1] % 359 == 0 or index[1] == 0:
                sys.stdout.write("\r{0} {1} {2}".format(*[index[0], index[1], index[2]]))
                sys.stdout.flush()

    print('\ndone with building polar image...')

    return spherical_matrix


def create_cartesian_matrix_from_polar(spherical_image, inital_cartesian_shape):

    cartesian_image = np.zeros(inital_cartesian_shape)

    for index, value in np.ndenumerate(cartesian_image):

        x = index[0] - int(np.floor(inital_cartesian_shape[0]/2))
        y = index[1] - int(np.floor(inital_cartesian_shape[1]/2))
        z = index[2] - int(np.floor(inital_cartesian_shape[2]/2))

        hxy = np.hypot(x, y)
        r = np.hypot(hxy, z)
        el = np.rad2deg(np.arctan2(z, hxy)) + 180
        az = np.rad2deg(np.arctan2(y, x)) + 180

        if 0 <= el < spherical_image.shape[0] and 0 <= az < spherical_image.shape[1] and 0 <= r < spherical_image.shape[2]:
            cartesian_image[index[0], index[1], inital_cartesian_shape[2] - 1 - index[2]] = interp_v2((el, az, r), spherical_image)
        else:
            cartesian_image[index[0], index[1], inital_cartesian_shape[2] - 1 - index[2]] = interp_v2((el, 0, r), spherical_image)

        if index[1] % 30 == 0 or index[1] == 0:
            sys.stdout.write("\r{0} {1} {2}".format(r, el, z))
            sys.stdout.flush()

    print('\ndone with building cartesian image...')

    return cartesian_image




