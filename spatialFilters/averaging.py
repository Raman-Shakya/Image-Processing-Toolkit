import cv2
from spatialFilters import baseKernel
import tkinter as tk
import numpy as np

class Averaging(baseKernel.BaseKernelFilter):
    def __init__(self):
        super().__init__("Averaging Filter", np.array([
            [1/9, 1/9, 1/9],
            [1/9, 1/9, 1/9],
            [1/9, 1/9, 1/9]
        ]))