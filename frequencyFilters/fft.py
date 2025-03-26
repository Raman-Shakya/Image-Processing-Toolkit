import tkinter as tk
from frequencyFilters.base import BaseFilterLayout

class FFT(BaseFilterLayout):
    def __init__(self):
        super().__init__("Fast Fourier Transform")

        self.button = tk.Button(self, text="Select Input", command=self.imageInput)
        self.button.pack()

        self.mainloop()

    def imageInput(self):
        self.readImage(grayScale=True)
        self.button.destroy()

        self.fourierTransform()
        self.inverseFourierTransform()
