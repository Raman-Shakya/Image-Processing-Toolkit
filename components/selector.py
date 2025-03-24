import tkinter as tk

class Selector(tk.Frame):
    def __init__(self, master, title, options=[]):
        super().__init__(master)
        self.pack()
        self.title = title
        self.options = options

        tk.Label(self, text=title).pack()
        self.render()

    def render(self):
        for option in self.options:
            label = tk.Button(self, text=option["title"], width=25, command=lambda callback=option["component"]: callback())
            label.pack()