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
        
        self.build_window()
        self.build_menu()
        self.pack()

    def start(self):
        self.master.mainloop()

    def build_window(self):
        self.popup_window.pack(side="top")
        self.pack()

    def refresh(self, headline, link):
        print("headline:", headline, "\nlink:", link)
        self.popup_window.configure(text=headline)
        self.popup_window.configure("<Button-1>", lambda e: webbrowser.open_new(link))

    def build_menu(self):
        self.menu_bar = tk.Menu(self)
        self.dropdown_menu = tk.Menu(self.menu_bar)
        self.color_menu = tk.Menu(self.dropdown_menu)
        list_colors = ["powder blue", "gray", "light green", "white"]
        for color in list_colors:
            self.color_menu.add_checkbutton(label=color, command=lambda arg0=color: RSSticker.background_color(arg0))
        self.dropdown_menu.add_command(label="Cycle Time", command=RSSticker.cycle_time())
        self.dropdown_menu.add_command(label="Window Placement", command=RSSticker.cycle_time())
        self.dropdown_menu.add_cascade(label="Change Background Color", menu=self.color_menu)
        self.menu_bar.add_cascade(label="Settings", menu=self.dropdown_menu)
        self.master.config(menu=self.menu_bar)

    def background_color(arg0):
        self.master.config(background=arg0)

    def cycle_time():
        pass
    
    def window_placment():
        pass

#if __name__ == "__main__":
    #root = tk.Tk()
    #root.title("RSSticker")
    #app = RSSticker(master=root)
    #RSSticker.build_menu()
   # app.mainloop()
