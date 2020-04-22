# references: https://www.youtube.com/watch?v=HxU_5LvkVrw
import tkinter
import feedparser
import webbrowser
import os
import tkinter as tk
from tkinter import ttk
from RSS.controller.rssfeed import RssController


class RSSticker(tk.Frame):
    time = None
    place = None
    color = None
    font_type = None
    font_size = None
    font_color = None

    def __init__(self, master=None):
        super().__init__(master)
        self.settings = {}
        self.T = tk.Text(self, font=("bold", 32,))
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
        placement_menu = tk.Menu(dropdown_menu)
        cycle_time_menu = tk.Menu(dropdown_menu)
        font_menu = tk.Menu(dropdown_menu)
        feed_menu = tk.Menu(dropdown_menu)
        list_colors = ["powder blue", "gray", "light green", "white"]
        list_placement = ["top left", "bottom left", "top right", "bottom right"]
        cycle_options = [5, 10, 15, 20, 25, 30]
        font_colors = ['blue', 'black', 'gold2', 'purple1']
        font_types = ['Times', 'Helvetica', 'Arial']
        font_sizes = [11, 12, 14, 16, 18, 20, 22, 24]
        feed_menu.add_radiobutton(label="show feeds", command= lambda: RSSticker.show_feeds())

        for color in font_colors:
            font_menu.add_radiobutton(label=color, command=lambda arg0=color: RSSticker.font_color(self, arg0))
        for color in list_colors:
            color_menu.add_radiobutton(label=color, command=lambda arg0=color: RSSticker.background_color(self, arg0))
        for time in cycle_options:
            cycle_time_menu.add_radiobutton(label=time, command=lambda arg0=time: RSSticker.cycle_time(self, arg0))
        for place in list_placement:
            placement_menu.add_radiobutton(label=place,
                                           command=lambda arg0=place: RSSticker.window_placement(self, arg0))
        dropdown_menu.add_cascade(label="Cycle Time", menu=cycle_time_menu)
        dropdown_menu.add_cascade(label="Window Placement", menu=placement_menu)
        dropdown_menu.add_cascade(label="Change Background Color", menu=color_menu)
        dropdown_menu.add_cascade(label="Change Font", menu=font_menu)
        dropdown_menu.add_cascade(label="Feeds", menu=feed_menu)
        menu_bar.add_cascade(label="Settings", menu=dropdown_menu)
        dropdown_menu.add_radiobutton(label="Save Settings",
                                      command=lambda: RSSticker.save(self, RSSticker.color,
                                                                     RSSticker.place,
                                                                     RSSticker.time))
        self.master.config(menu=menu_bar)

    def background_color(self, arg0):
        RSSticker.color = arg0
        self.master.configure(background=arg0)

    def cycle_time(self, arg0):
        RSSticker.time = arg0
        pass

    def window_placement(self, arg0):
        RSSticker.place = arg0
        if arg0 == "top left":
            self.master.geometry("+0+0")
        elif arg0 == "bottom left":
            self.master.geometry("+0+750")
        elif arg0 == "top right":
            self.master.geometry("+1000+0")
        elif arg0 == "bottom right":
            self.master.geometry("+1000+750")

    def font_color(self, color):
        pass

    def save(self, color, place, time):
        self.settings = {'background_color': color, 'window placement': place, 'cycle_time': time}
        _rss = RssController()
        _rss.save_settings(self.settings)

    def show_feeds(self, feeds):
        for feed in feeds:
            field = feed[0]
            text = feed[1].get()
            print(field, text)

    def add_feed(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("RSSticker")
    app = RSSticker(master=root)
    app.mainloop()
