import cv2
from spatialFilters import baseKernel
import tkinter as tk
import numpy as np

class PrewittFilter(baseKernel.BaseKernelFilter):
    def __init__(self):
        super().__init__("Prewitt Filter", np.array([
            [-1, -1, -1],
            [0, 0, 0],
            [1, 1, 1]
        ]))