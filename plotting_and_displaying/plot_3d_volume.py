import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_3d_image(image):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(image)

    plt.show()


def plot_2d_image(image):
    plt.imshow(image, cmap='gray')
    plt.show()









