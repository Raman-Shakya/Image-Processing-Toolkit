import tkinter as tk


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