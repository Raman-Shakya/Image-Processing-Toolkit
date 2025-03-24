import cv2
from spatialFilters import base
import tkinter as tk

class DigitalNegative(base.BaseFilterLayout):
    def __init__(self):
        super().__init__("Digital Negative")

        self.button = tk.Button(self, text="Select Input", command=self.imageInput)
        self.button.pack()

        self.mainloop()

    def imageInput(self):
        self.readImage()
        self.button.destroy()

        output = self.input_image[0]
        output = 255 - output

        self.addOutput(output)