import tkinter as tk
from components.selector import Selector
from spatialFilters import digitalNegative, base

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack( padx=5, pady=5, side=tk.TOP)

        Selector(self, title="Image Enhancement and Filter in Spatial Domain", options=[
            {
                "title": "Point Operations",
                "component": base.BaseFilterLayout
            },
            {
                "title": "Contrast Stretching",
                "component": base.BaseFilterLayout
            },
            {
                "title": "Digital Negative",
                "component": digitalNegative.DigitalNegative
            }
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