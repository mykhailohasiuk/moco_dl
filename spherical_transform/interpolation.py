import numpy as np



def distance3d(ax, ay, az, bx, by, bz):
    return np.sqrt(np.square(ax-bx) + np.square(ay-by) + np.square(az-bz))


def distance_weighted_value(d1, d2, d3, d4, d5, d6, d7, d8, v1, v2, v3, v4, v5, v6, v7, v8):

    distance_mult = d1*d2*d3*d4*d5*d5*d6*d7*d8
    mediated_value = (v1/d1) + (v2/d2) + (v3/d3) + (v4/d4) + (v5/d5) + (v6/d6) + (v7/d7) + (v8/d8)

    return distance_mult*mediated_value

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

    # calculating the distances to the 8 nearest neighbours:

    dist_x0_y1_z1 = distance3d(pointx, pointy, pointz, closest_x0, closest_y1, closest_z1)
    dist_x0_y1_z0 = distance3d(pointx, pointy, pointz, closest_x0, closest_y1, closest_z0)
    dist_x0_y0_z1 = distance3d(pointx, pointy, pointz, closest_x0, closest_y0, closest_z1)
    dist_x0_y0_z0 = distance3d(pointx, pointy, pointz, closest_x0, closest_y0, closest_z0)

    dist_x1_y1_z1 = distance3d(pointx, pointy, pointz, closest_x1, closest_y1, closest_z1)
    dist_x1_y1_z0 = distance3d(pointx, pointy, pointz, closest_x1, closest_y1, closest_z0)
    dist_x1_y0_z1 = distance3d(pointx, pointy, pointz, closest_x1, closest_y0, closest_z1)
    dist_x1_y0_z0 = distance3d(pointx, pointy, pointz, closest_x1, closest_y0, closest_z0)

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

    point_value = distance_weighted_value(dist_x0_y1_z1,dist_x0_y1_z0,dist_x0_y0_z1,dist_x0_y0_z0,
                                          dist_x1_y1_z1,dist_x1_y1_z0,dist_x1_y0_z1,dist_x1_y0_z0,

                                          val_x0_y1_z1,val_x0_y1_z0,val_x0_y0_z1,val_x0_y0_z0,
                                          val_x1_y1_z1,val_x1_y1_z0,val_x1_y0_z1,val_x1_y0_z0)

    return point_value

# data = np.array(
#     [
#         [
#             [0,1,2],
#             [3,4,5],
#             [6,7,8]
#         ],
#         [
#             [0,1,2],
#             [3,4,5],
#             [6,7,8]
#         ]
#      ]
# )
# print(data.shape)
#
# point = np.array([0.4, 0.8, 0.2])
#
# value = interpn(point, data, np.array(point).T)
# print(value)