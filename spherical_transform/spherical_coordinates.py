import numpy as np
import math

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


def appendSpherical_np(xyz):
    ptsnew = np.array(np.zeros(xyz.shape))
    xy = xyz[:,0]**2 + xyz[:,1]**2
    ptsnew[:,0] = np.sqrt(xy + xyz[:,2]**2)
    ptsnew[:,1] = np.arctan2(np.sqrt(xy), xyz[:,2]) # for elevation angle defined from Z-axis down
    #ptsnew[:,1] = np.arctan2(xyz[:,2], np.sqrt(xy)) # for elevation angle defined from XY-plane up
    ptsnew[:,2] = np.arctan2(xyz[:,1], xyz[:,0])
    return ptsnew


def find_spherical_matrix_dimensions(cartesian_image_shape):
    theta = 360
    phi = 360
    hxy = np.hypot(cartesian_image_shape[0], cartesian_image_shape[1])
    r = int(math.ceil(np.hypot(hxy, cartesian_image_shape[2])))

    return (theta, phi, r)


def create_spherical_matrix_from_cartesian(cartesian_image):

    spherical_image = np.zeros((find_spherical_matrix_dimensions(cartesian_image.shape)))
    print('spherical matrix shape: ', spherical_image.shape)

    for az in range(spherical_image.shape[0]):
        for el in range(spherical_image.shape[1]):
            for r in range(spherical_image.shape[2]):
                x, y, z = int(math.floor(sph2cart(az, el, r)[0])), int(math.floor(sph2cart(az, el, r)[1])), int(math.floor(sph2cart(az, el, r)[2]))
                print('-----looking for coordiantes: ', x, y, z, '\n')
                # spherical_image[r, el, az] = cartesian_image[x, y, z]
        print(r)
    return spherical_image


testImage = create_spherical_matrix_from_cartesian(np.zeros((64, 64, 64)))
print(testImage.shape)


