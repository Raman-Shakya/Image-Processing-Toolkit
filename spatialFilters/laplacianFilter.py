import cv2
from spatialFilters import baseKernel
import tkinter as tk
import numpy as np

class LaplacianFilter(baseKernel.BaseKernelFilter):
    def __init__(self):
        super().__init__("Laplacian Filter", np.array([
            [0, 1, 0],
            [1, -4, 1],
            [0, 1, 0]
        ]))