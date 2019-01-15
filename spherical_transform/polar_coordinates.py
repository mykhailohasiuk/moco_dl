import numpy as np


def find_polar_dimensions(cartesian_image_shape):
    phi = 360
    r = int(np.floor((np.hypot(cartesian_image_shape[0], cartesian_image_shape[1]))/2))

    return phi, r


def find_2d_cartesian_dimensions(cartesian_image_shape):
    x = y = np.int(np.floor(2 * cartesian_image_shape[-1]/np.sqrt(2)))

    return x, y



def factor(d):
    eps = 1e-6
    return (1+eps)/(d+eps)


def distance2d(ax, ay, bx, by):
    return np.sqrt(np.square(ax-bx) + np.square(ay-by))


def reverse_distance_weighted_value(d1, d2, d3, d4, v1, v2, v3, v4):

    mediated_value = (v1 * factor(d1)) + (v2 * factor(d2)) + (v3 * factor(d3)) + (v4 * factor(d4))
    distance_mult = d1 * d2 * d3 * d4

    return mediated_value * distance_mult


def interpolate_2d_point(point, array_2d):

    pointx = point[0]
    pointy = point[1]

    closest_x0 = np.floor(pointx)
    closest_x1 = np.ceil(pointx)

    closest_y0 = np.floor(pointy)
    closest_y1 = np.ceil(pointy)

    cubical_1 = np.sqrt(2)

    # calculating reversed distances to the 4 nearest neighbours:

    dist_x0_y1 = cubical_1 - distance2d(pointx, pointy, closest_x0, closest_y1)
    dist_x0_y0 = cubical_1 - distance2d(pointx, pointy, closest_x0, closest_y0)

    dist_x1_y1 = cubical_1 - distance2d(pointx, pointy, closest_x1, closest_y1)
    dist_x1_y0 = cubical_1 - distance2d(pointx, pointy, closest_x1, closest_y0)

    ind_x0 = np.int(closest_x0)
    ind_x1 = np.int(closest_x1)

    ind_y0 = np.int(closest_y0)
    ind_y1 = np.int(closest_y1)

    val_x0_y1 = array_2d[ind_x0, ind_y1]
    val_x0_y0 = array_2d[ind_x0, ind_y0]

    val_x1_y1 = array_2d[ind_x1, ind_y1]
    val_x1_y0 = array_2d[ind_x1, ind_y0]

    point_value = reverse_distance_weighted_value(dist_x0_y1, dist_x0_y0, dist_x1_y1, dist_x1_y0,
                                                  val_x0_y1, val_x0_y0, val_x1_y1, val_x1_y0)

    return point_value


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


def create_cartesian_2d_image(polar_image):
    polar_shape = polar_image.shape
    x, y = find_2d_cartesian_dimensions(polar_shape)
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
