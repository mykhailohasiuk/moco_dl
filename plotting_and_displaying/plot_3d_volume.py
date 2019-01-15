import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import nibabel as nib


def plot_3d_image(image):
    print ('\nBuilding a graph...')
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(image)

    plt.show()


def plot_nib_3d(image):
    print ('\nBuilding a graph...')
    nib.viewers.OrthoSlicer3D(image).show()


def plot_2d_image(image, cmap='gray'):
    print ('\nBuilding a graph...')
    plt.imshow(image, cmap=cmap)
    plt.show()









