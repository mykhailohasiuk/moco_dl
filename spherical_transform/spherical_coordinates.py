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

def factor(d):
    eps = 1e-6
    return (1+eps)/(d+eps)


def distance3d(ax, ay, az, bx, by, bz):
    return np.sqrt(np.square(ax-bx) + np.square(ay-by) + np.square(az-bz))


def reverse_distance_weighted_value(d1, d2, d3, d4, d5, d6, d7, d8, v1, v2, v3, v4, v5, v6, v7, v8):

    distance_mult = factor(d1) * factor(d2) * factor(d3) * factor(d4) * factor(d5) * factor(d5) * factor(d6) * factor(d7) * factor(d8)

    mediated_value = v1 * factor(d1) + v2 * factor(d2) + v3 * factor(d3) + v4 * factor(d4) + \
                     v5 * factor(d5) + v6 * factor(d6) + v7 * factor(d7) + v8 * factor(d8)

    return mediated_value/distance_mult

    # return d1*v1 + d2*v2 + d3*v3 + d4*v4 + d5*v5 + d6*v6 + d7*v7 + d8*v8


def interpolate_3d_point(point, array_3d):

    pointx = point[0]
    pointy = point[1]
    pointz = point[2]

    closest_x0 = np.floor(pointx)
    closest_x1 = np.ceil(pointx)

    closest_y0 = np.floor(pointy)
    closest_y1 = np.ceil(pointy)

    closest_z0 = np.floor(pointz)
    closest_z1 = np.ceil(pointz)

    cubical_1 = np.sqrt(3)

    # calculating reversed distances to the 8 nearest neighbours:

    dist_x0_y1_z1 = cubical_1 - distance3d(pointx, pointy, pointz, closest_x0, closest_y1, closest_z1)
    dist_x0_y1_z0 = cubical_1 - distance3d(pointx, pointy, pointz, closest_x0, closest_y1, closest_z0)
    dist_x0_y0_z1 = cubical_1 - distance3d(pointx, pointy, pointz, closest_x0, closest_y0, closest_z1)
    dist_x0_y0_z0 = cubical_1 - distance3d(pointx, pointy, pointz, closest_x0, closest_y0, closest_z0)

    dist_x1_y1_z1 = cubical_1 - distance3d(pointx, pointy, pointz, closest_x1, closest_y1, closest_z1)
    dist_x1_y1_z0 = cubical_1 - distance3d(pointx, pointy, pointz, closest_x1, closest_y1, closest_z0)
    dist_x1_y0_z1 = cubical_1 - distance3d(pointx, pointy, pointz, closest_x1, closest_y0, closest_z1)
    dist_x1_y0_z0 = cubical_1 - distance3d(pointx, pointy, pointz, closest_x1, closest_y0, closest_z0)

    ind_x0 = np.int(closest_x0)
    ind_x1 = np.int(closest_x1)

    ind_y0 = np.int(closest_y0)
    ind_y1 = np.int(closest_y1)

    ind_z0 = np.int(closest_z0)
    ind_z1 = np.int(closest_z1)

    val_x0_y1_z1 = array_3d[ind_x0, ind_y1, ind_z1]
    val_x0_y1_z0 = array_3d[ind_x0, ind_y1, ind_z0]
    val_x0_y0_z1 = array_3d[ind_x0, ind_y0, ind_z1]
    val_x0_y0_z0 = array_3d[ind_x0, ind_y0, ind_z0]

    val_x1_y1_z1 = array_3d[ind_x1, ind_y1, ind_z1]
    val_x1_y1_z0 = array_3d[ind_x1, ind_y1, ind_z0]
    val_x1_y0_z1 = array_3d[ind_x1, ind_y0, ind_z1]
    val_x1_y0_z0 = array_3d[ind_x1, ind_y0, ind_z0]

    point_value = reverse_distance_weighted_value(dist_x0_y1_z1, dist_x0_y1_z0, dist_x0_y0_z1, dist_x0_y0_z0,
                                                  dist_x1_y1_z1, dist_x1_y1_z0, dist_x1_y0_z1, dist_x1_y0_z0,

                                                  val_x0_y1_z1, val_x0_y1_z0, val_x0_y0_z1, val_x0_y0_z0,
                                                  val_x1_y1_z1, val_x1_y1_z0, val_x1_y0_z1, val_x1_y0_z0)

    return point_value


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

        if 0 <= x < cart_shape[0]-1 and 0 <= y < cart_shape[1]-1 and 0 <= z < cart_shape[2]-1:

            if index[1] % 359 == 0 or index[1]  == 0:
                sys.stdout.write("\r{0} {1} {2}".format(*index))
                sys.stdout.flush()

            sph_img[index[0], index[1], index[2]] = interpolate_3d_point((x, y, z), cartesian_image)

    print('\nDone with creating polar image... \n Building a graph...')
    return sph_img




