import tkinter as tk

class ControlWindow(tk.Tk):
    def __init__(self, geometry="400x400"):
        super().__init__()
        self.title("Command Window")
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def create_button(self, text, button_callback, width=25, pady=10):
        button = tk.Button(text=text, command=button_callback, width=width, pady=pady)
        button.pack(side=tk.TOP)