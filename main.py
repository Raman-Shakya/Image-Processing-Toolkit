import tkinter as tk
from components.selector import Selector
from spatialFilters import digitalNegative, averaging, base, laplacianFilter, prewittFilter, sobelFilter

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack( padx=5, pady=5, side=tk.TOP)

        Selector(self, title="Image Enhancement and Filter in Spatial Domain", options=[
            {
                "title": "Digital Negative",
                "component": digitalNegative.DigitalNegative
            },
            {
                "title": "Averaging Filter",
                "component": averaging.Averaging
            },
            {
                "title": "Laplacian Filter",
                "component": laplacianFilter.LaplacianFilter
            },
            {
                "title": "Prewitt Filter",
                "component": prewittFilter.PrewittFilter
            },
            {
                "title": "Sobel Filter",
                "component": sobelFilter.SobelFilter
            },
        ])

        Selector(self, title="Image Enhancement and Filter in Frequency Domain", options=[
            {
                "title": "hello",
                "component": base.BaseFilterLayout
            },
            {
                "title": "hello",
                "component": base.BaseFilterLayout
            },
            {
                "title": "hello",
                "component": base.BaseFilterLayout
            }
        ])


def main():
    root = tk.Tk()
    root.title("Image Processing Toolkit")
    root.geometry("400x300")

    app = App(root)

    root.mainloop()

if __name__=="__main__":
    main()