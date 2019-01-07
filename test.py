from spherical_transform.spherical_coordinates import *
from spherical_transform.polar_coordinates import *
from spherical_transform.sphere_creation import *
from scipy.ndimage import shift
from plotting_and_displaying.plot_3d_volume import plot_3d_image, plot_2d_image, plot_nib_3d
from mpl_toolkits.mplot3d import Axes3D
from nibabel.viewers import OrthoSlicer3D
import nibabel as nib

import matplotlib.pyplot as plt

input_sphere = create_3d_circle(32, 16, 1)
#
float_sphere = input_sphere.astype(float)
#
#
new_circle = np.zeros(float_sphere.shape)
new_circle[0,:,:] = float_sphere[16,:,:]

plot_3d_image(new_circle)
# # plot_3d_image(input_sphere)
# # print(float_circle.shape)
# shifted_sphere = shift(float_sphere, [-4, 0, 0])
#
# spherical_image = create_spherical_matrix_from_cartesian(float_sphere)
# # print(spherical_image.shape)
#
# # data = np.array(
# #     [
# #         [
# #             [0,1,2],
# #             [3,4,5],
# #             [6,7,8]
# #         ],
# #         [
# #             [0,1,2],
# #             [3,4,5],
# #             [6,7,8]
# #         ]
# #      ]
# # )
# np.save('./outputs/spherical_circle_shifted_interpolated1', spherical_image)
# img = np.load('./outputs/spherical_circle_interpolated1.npy')
nib.save(nib.Nifti1Image(new_circle, affine=None), 'shifted_circle_cartesian.nii')

# sphere = np.load('outputs/spherical_interpolated1.npy')

# a = np.sin(np.linspace(0, np.pi, 20))

# b = np.sin(np.linspace(0, np.pi*5, 20))
# data = np.outer(a, b)[..., np.newaxis] * a
# OrthoSlicer3D(data).show()

# image = np.load('./outputs/spher_sphere.npy')



# np.save('./outputs/spher_circle', spherical_image)

# circle = create_circle(64, 30, 1)
# shifted_circle = shift(circle, [-32, -32])


# polar_circle = create_polar_image(circle)

# plot_2d_image(polar_circle)

