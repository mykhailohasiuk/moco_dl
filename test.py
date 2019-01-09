from spherical_transform.spherical_coordinates import *
from spherical_transform.polar_coordinates import *
from spherical_transform.sphere_creation import *
from scipy.ndimage import shift, rotate
from plotting_and_displaying.plot_3d_volume import plot_3d_image, plot_2d_image, plot_nib_3d
import numpy as np

import nibabel as nib

import matplotlib.pyplot as plt

input_img = create_3d_circle(32, 15, 3).astype(float)
# rot_img = np.round(rotate(input_img, -45, [0, 1], reshape=False))

# rot_img = input_img
#
spherical_image = np.load('/Users/mhas0023/dev/DL_spherical/spherical_circle_try_3.npy')
# np.save('./outputs/spherical_sphere_aproach_2', spherical_image)
# spherical_image = np.load('spherical_circle_try_1.npy')
# np.save('./outputs/3d_circle_aproach_2', spherical_image)
# plot_3d_image(spherical_image)
# nib.save(nib.Nifti1Image(spherical_image, affine=None), 'circle_sph_test_2.nii')
# nib.save(nib.Nifti1Image(input_img, affine=None), 'circle_cart_test_2.nii')
# plot_3d_image(spherical_image)
# print(str(np.deg2rad(270) / np.pi) + 'Pi')
# plot_2d_image(spherical_image[:,:,14])

# spherical_image = create_spherical_matrix_from_cartesian(input_img)
# np.save('spherical_circle_try_3', spherical_image)
# nib.save(nib.Nifti1Image(spherical_image, affine=None), 'spherical_circle_3.nii')

#
recreated_cartesian = recreate_cartesian_image(spherical_image)
np.save('recreated_cartesian_try_2', recreated_cartesian)
nib.save(nib.Nifti1Image(recreated_cartesian, affine=None), 'recreated_cart_circle_2.nii')

# circle = create_circle(128, 60, 10)
# plt.imshow(circle)
# plt.show()
# polar_circle = create_polar_image(circle)
# plt.imshow(polar_circle)
# plt.show()
# recreated_circle = create_cartesian_image(polar_circle)
# plt.imshow(recreated_circle)
# plt.show()