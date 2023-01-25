from tkinter import Entry, StringVar, Label, Button, OptionMenu, Canvas
from PIL import ImageTk, Image
from tkinter.ttk import Scrollbar

class TkinterController:
    def return_entry_field(self, text, callback_command, width, posx, posy, bg="#FF5733", fg='#E0E0E0'):
        string_var = StringVar()
        string_var.trace("w", lambda name, index, mode, var=string_var: callback_command(string_var))
        entry_field = Entry(text=text, textvariable=string_var)
        entry_field.insert(0, text)
        entry_field.config(width=width)
        entry_field.place(x=posx, y=posy)
        return entry_field

    def place_image(self, gui, image_path, posx, posy, size=None):
        card_image = Image.open(image_path)
        if not size is None:
            card_image = card_image.resize((size))
        render = ImageTk.PhotoImage(card_image)

        label = Label(gui, image=render)
        label.image = render
        label.place(x=posx, y=posy)

    def add_button(self, gui, text, callback_command, width, height, posx, posy, bg="#FF5733", fg='#E0E0E0'):
        button = Button(gui, text=text, command=callback_command, bg=bg, fg=fg)
        button.config(width=width, height=height)
        button.place(x=posx, y=posy)
        return button

    def add_card_button(self, gui, text, callback_command, pady, width, posx, posy, card, section, max_in_section):
        button = Button(gui, text=text, command=lambda: callback_command(card, section, max_in_section))
        button.pack(pady=pady)
        button.config(width=width)
        button.place(x=posx, y=posy)
        return button

    def add_dropdown(self, gui, options, pady, width, posx, posy, callback):
        variable = StringVar(gui)
        variable.set(options[0])
        variable.trace("w", lambda name, index, mode, var=variable: callback(var))

        options_menu = OptionMenu(gui, variable, *options)
        options_menu.pack(pady=pady)
        options_menu.place(x=posx, y=posy)
        options_menu.config(width=width)
        return options_menu


    def clear_gui(self, gui):
        for widget in gui.winfo_children():
            widget.destroy()