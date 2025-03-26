import tkinter as tk
from tkinter.filedialog import askopenfilename
import cv2
from components.imageList import ImageLists
import numpy as np

class BaseFilterLayout(tk.Tk):
    def __init__(self, name):
        super().__init__()
        self.title(name)
        self.geometry("400x300")

        self.input_image = []
        self.output_image = []

        self.imageContainer = ImageLists(self, "./temp_input/input-")
        self.outputContainer = ImageLists(self, "./temp_output/output-")


    def readImage(self, grayScale=False):
        filePath = askopenfilename()
        image = cv2.imread(filePath)
        if grayScale:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        aspect = len(image) / len(image[0])
        height = 300
        image = cv2.resize(image, (int(height/aspect), height), interpolation=cv2.INTER_LINEAR)
        
        cv2.imwrite(f"temp_input/input-{len(self.input_image)}.png", image)
        self.input_image.append(image)

        self.imageContainer.addImage(len(self.input_image)-1)


    def fourierTransform(self):
        self.fft = np.fft.fft2(self.input_image[0])
        fft_shift = np.fft.fftshift(self.fft)

        self.addOutput(20 * np.log(np.abs(fft_shift) + 1))

    def inverseFourierTransform(self):
        inverseFFT = np.fft.ifft2(self.fft)
        self.addOutput(np.abs(inverseFFT))

        

    def addOutput(self, output):
        cv2.imwrite(f"temp_output/output-{len(self.output_image)}.png", output)
        self.outputContainer.addImage(0)
        self.geometry("400x900")

