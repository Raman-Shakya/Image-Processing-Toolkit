import cv2
from spatialFilters import base
import tkinter as tk
import numpy as np

class BaseKernelFilter(base.BaseFilterLayout):
    def __init__(self, name, kernel):
        super().__init__(name)

        self.button = tk.Button(self, text="Select Input", command=self.imageInput)
        self.button.pack()
        self.kernel = kernel

        self.mainloop()

    def imageInput(self):
        self.readImage(grayScale=True)
        self.button.destroy()

        output = self.calculateOutput()

        self.addOutput(output)


    def calculateOutput(self):
        output = []
        for i in range(1, len(self.input_image[0])-2):
            temp = []
            for j in range(1, len(self.input_image[0][0])-2):
                temp.append(sum(self.kernel * self.input_image[0][i-1:i+2, j-1:j+2]))
            output.append(temp)
        return np.array(output)