from spherical_transform.spherical_coordinates import *
from spherical_transform.polar_coordinates import *
from spherical_transform.sphere_creation import *
from scipy.ndimage import shift
from plotting_and_displaying.plot_3d_volume import plot_3d_image, plot_2d_image
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

input_sphere = create_3d_circle(20, 8, 1)
# input_sphere = shift(input_sphere, [-16, -16, -16])

# spherical_sphere = appendSpherical_np(input_sphere)

spherical_image = create_spherical_matrix_from_cartesian(input_sphere)


# plot_3d_image(input_sphere)
plot_3d_image(spherical_image)

# image = np.load('./outputs/spher_sphere.npy')



# np.save('./outputs/spher_circle', spherical_image)

# circle = create_circle(64, 30, 1)
# shifted_circle = shift(circle, [-32, -32])


# polar_circle = create_polar_image(circle)

# plot_2d_image(polar_circle)

