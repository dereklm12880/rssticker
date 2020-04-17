import tkinter
import feedparser
import webbrowser
import os
import tkinter as tk
from tkinter import ttk


class RSSticker(tk.Frame):
    headline = "[insert headline here]"

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.popup_window = ttk.Label(self.master)
        self.build_menu()
        self.pack()


    def build_window(self):
        self.popup_window.pack(side="top")
        self.pack()

    def refresh(self, headline, link):
        self.popup_window.configure(text=headline)
        self.popup_window.configure("<Button-1>", lambda e: webbrowser.open_new(link))

    # def style(self):
    # will show styled window

    def build_menu(self):
        menu_bar = tk.Menu(root)
        dropdown_menu = tk.Menu(menu_bar)
        color_menu = tk.Menu(dropdown_menu)
        cycle_time_menu = tk.Menu(dropdown_menu)
        list_colors = ["powder blue", "gray", "light green", "white"]
        for color in list_colors:
            color_menu.add_checkbutton(label=color, command=lambda arg0=color: RSSticker.background_color(arg0))
        cycle_options = [5, 10, 15, 20, 25, 30]
        for time in cycle_options:
            cycle_time_menu.add_checkbutton(label=time, command=lambda arg0=time: RSSticker.cycle_time(arg0))
        dropdown_menu.add_cascade(label="Cycle Time", menu=cycle_time_menu)
        dropdown_menu.add_command(label="Window Placement", command=RSSticker.window_placment())
        dropdown_menu.add_cascade(label="Change Background Color", menu=color_menu)
        menu_bar.add_cascade(label="Settings", menu=dropdown_menu)
        root.config(menu=menu_bar)

    def background_color(arg0):
        root.configure(background=arg0)

    def cycle_time(arg0):
        pass

    def window_placment():
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("RSSticker")
    app = RSSticker(master=root)
    app.mainloop()
