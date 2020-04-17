import tkinter
import feedparser
import webbrowser
import os
import tkinter as tk
from tkinter import ttk

class RSSticker(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.popup_window = ttk.Label(master)

        self.build_window()
        self.build_menu()
        self.pack()
    
    def start(self):
        self.master.mainloop()

    def build_window(self):
        self.popup_window.pack(side="top")

    def refresh(self, headline, link):
        print("headline:", headline, "\nlink:", link)
        self.popup_window.configure(text=headline)
        self.popup_window.configure("<Button-1>", lambda e: webbrowser.open_new(link))

    def build_menu(self):
        menu_bar = tk.Menu(self.popup_window)
        dropdown_menu = tk.Menu(menu_bar)
        color_menu = tk.Menu(dropdown_menu)
        cycle_time_menu = tk.Menu(dropdown_menu)
        list_colors = ["powder blue", "gray", "light green", "white"]
        for color in list_colors:
            color_menu.add_checkbutton(label=color, command=lambda arg0=color: RSSticker.background_color(arg0))
        cycle_time_menu.add_command(label="Cycle Time", command=RSSticker.cycle_time())
        dropdown_menu.add_command(label="Window Placement", command=RSSticker.cycle_time())
        dropdown_menu.add_cascade(label="Cycle Time", menu=cycle_time_menu)
        dropdown_menu.add_cascade(label="Change Background Color", menu=color_menu)
        menu_bar.add_cascade(label="Settings", menu=dropdown_menu)
        self.popup_window.config(menu=menu_bar)

    def background_color(self, arg0):
        self.popup_window.configure(background=arg0)

    def cycle_time():
        pass

    def window_placment():
        pass
