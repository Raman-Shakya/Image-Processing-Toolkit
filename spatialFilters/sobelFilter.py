import cv2
from spatialFilters import baseKernel
import tkinter as tk
import numpy as np

class SobelFilter(baseKernel.BaseKernelFilter):
    def __init__(self):
        super().__init__("Sobel Filter", np.array([
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]
        ]))