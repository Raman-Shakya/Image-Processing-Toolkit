import cv2
from spatialFilters import baseKernel
import tkinter as tk
import numpy as np

class SobelFilter(baseKernel.BaseKernelFilter):
    def __init__(self):
        super().__init__("Sobel Filter", [])

    def calculateOutput(self):
        self.kernelx = np.array([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ])
        self.kernely = np.array([
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]
        ])

        magnitude = []
        total = 0
        for i in range(1, len(self.input_image[0])-2):
            temp = []
            for j in range(1, len(self.input_image[0][0])-2):
                tempx = sum(sum(self.kernelx * self.input_image[0][i-1:i+2, j-1:j+2]))
                tempy = sum(sum(self.kernely * self.input_image[0][i-1:i+2, j-1:j+2]))
                temp_mag = ((tempx)**2 + (tempy)**2) ** .5
                total += temp_mag
                temp.append(temp_mag)
            magnitude.append(temp)

        threshold = total / (len(magnitude) * len(magnitude[0]))
        print(threshold)

        for i in range(len(magnitude)):
            for j in range(len(magnitude[0])):
                if magnitude[i][j] > threshold: magnitude[i][j] = 255
                else:
                    magnitude[i][j] = 0
        return np.array(magnitude)