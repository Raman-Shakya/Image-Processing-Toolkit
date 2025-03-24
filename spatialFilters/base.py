import tkinter as tk
from tkinter.filedialog import askopenfilename
import cv2

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

    def addOutput(self, output):
        cv2.imwrite(f"temp_output/output-{len(self.output_image)}.png", output)
        self.outputContainer.addImage(0)
        self.geometry("400x600")


class ImageLists(tk.Frame):
    def __init__(self, master, path):
        super().__init__(master)
        self.pack()
        self.path = path
        self.images = []

    def addImage(self, imageIndex):
        image = tk.PhotoImage(master=self, file=f"{self.path}{imageIndex}.png")
        self.images.append(image)
        tk.Label(self, image=image).pack()