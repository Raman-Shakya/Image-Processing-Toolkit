import cv2
from spatialFilters import baseKernel
import tkinter as tk
import numpy as np

class HistogramEqualization(baseKernel.BaseKernelFilter):
    def __init__(self):
        super().__init__("Histogram Equalization", [])

    def calculateOutput(self):
        histogram = [0 for _ in range(256)]
        for i in range(len(self.input_image[0])):
            for j in range(len(self.input_image[0][0])):
                histogram[int(self.input_image[0][i][j])] += 1
                
        # stretching part
        left_end = 0
        while histogram[left_end]==0: left_end+=1
        right_end = 255
        while histogram[right_end]==0: right_end-=1

        histogramMap1 = [0 for _ in range(256)]
        histogram1 = [0 for _ in range(256)]
        for i in range(left_end, right_end):
            temp_ind = int(255 / (right_end - left_end) * (i - left_end))
            histogramMap1[i] = temp_ind
            histogram1[temp_ind] += histogram[i]


        # equalization
        previous = 0
        totalPixels = len(self.input_image[0]) * len(self.input_image[0][0])

        histogramMap2 = [0 for _ in range(256)]
        for i,j in enumerate(histogram1):
            previous += j / totalPixels
            histogramMap2[i] = round(previous * 255)

        output = []
        for i in range(len(self.input_image[0])):
            temp = []
            for j in range(len(self.input_image[0][0])):
                temp.append(histogramMap2[histogramMap1[int(self.input_image[0][i][j])]])
            output.append(temp)


        return np.array(output)
    
