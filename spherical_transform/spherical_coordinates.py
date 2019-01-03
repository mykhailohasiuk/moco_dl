import numpy as np

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

def to_spherical_from_imge_center(image):
    image_center_x, image_center_y, image_center_z = image.shape[0]/2, image.shape[1]/2, image.shape[2]/2

    spherical_image = np.zeros(image.shape)

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            for z in range(image.shape[2]):
                point_x = x - image_center_x
                point_y = y - image_center_y
                point_z = z - image_center_z

                r, el, az = cart2sph(point_x, point_y, point_z)

