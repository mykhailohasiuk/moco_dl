from spherical_transform.spherical_coordinates import *
from spherical_transform.sphere_creation import *

import numpy as np
import matplotlib as mtplt
import matplotlib.pyplot as plt

input_sphere = create_sphere(64, 20, 1)

spherical_sphere = appendSpherical_np(input_sphere)
print(spherical_sphere.shape)

plt.imshow(spherical_sphere[:,32,:])
plt.show()


