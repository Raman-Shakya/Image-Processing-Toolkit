import cv2
from spatialFilters import baseKernel
import tkinter as tk
import numpy as np

class GaussianBlur(baseKernel.BaseKernelFilter):
    def __init__(self):
        super().__init__("Gaussian Blur", np.array([
            [1/16, 2/16, 1/16],
            [2/16, 4/16, 2/16],
            [1/16, 2/16, 1/16]
        ]))