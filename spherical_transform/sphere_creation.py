import pymrt as mrt
import pymrt.geometry
import numpy as np


def create_sphere(field_size, radius, thickness=1):
    outer_shape = mrt.geometry.sphere(field_size, radius)
    inner_shape = mrt.geometry.sphere(field_size, radius-thickness)

    sphere = np.array(outer_shape)

    for x in range(inner_shape.shape[0]):
        for y in range(inner_shape.shape[1]):
            for z in range(inner_shape.shape[2]):
                if inner_shape[x, y, z]:
                    sphere[x, y, z] = False
    return sphere
