from RSS.model.style import style_default

2  # references: https://www.youtube.com/watch?v=HxU_5LvkVrw
import tkinter
import feedparser
import webbrowser
import os, sys
import tkinter as tk
from tkinter import ttk
from pathlib import Path

sys.path.append("../../")
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
        # self.style()
        self.pack()
        self.build_window()
        self.default = ['white', 'top left', 5]
        self.i = 0

    def start(self):
        self.master.mainloop()

    def start(self):
        self.master.mainloop()

    # def style(self):
    #
    #     ctr = RssController()
    #     # if 'background_color' in ctr.settings_model.settings:
    #     #     RSSticker.color = ctr.settings_model.settings['background_color']
    #     # else:
    #     #     RSSticker.color = 'white'  # or whatever default value
    #     #
    #     if 'cycle_time' in ctr.settings_model.settings:
    #         RSSticker.time = ctr.settings_model.settings['cycle_time']
    #     else:
    #         RSSticker.time = 5  # or whatever default value
    #     #
        # if 'font_color' in ctr.settings_model.settings:
        #     RSSticker.font_color = ctr.settings_model.settings['font_color']
        # else:
        #     RSSticker.color = '#000000'  # or whatever default value
        #
        # if 'font_size' in ctr.settings_model.settings:
        #     RSSticker.font_size = ctr.settings_model.settings['font_size']
        # else:
        #     RSSticker.font_size = '12pt'  # or whatever default value
        #
        # if 'font_type' in ctr.settings_model.settings:
        #     RSSticker.font_type = ctr.settings_model.settings['font_type']
        # else:
        #     RSSticker.font_type = 'Times New Roman'  # or whatever default value
        #
        # if 'window placement' in ctr.settings_model.settings:
        #     RSSticker.window_placement = ctr.settings_model.settings['window placement']
        # else:
        #     RSSticker.window_placement = 'top left'  # or whatever default value

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
        list_colors = ["powder blue", "gray", "light green", "white"]
        list_placement = ["top left", "bottom left", "top right", "bottom right"]
        cycle_options = [5, 10, 15, 20, 25, 30]
        font_colors = ['blue', 'black', 'gold2', 'purple1']
        font_types = ['Times', 'Helvetica', 'Arial']
        font_sizes = [11, 12, 14, 16, 18, 20, 22, 24]
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
        _rss = RssController()
        self.settings = {'background_color': color, 'window placement': place, 'cycle_time': time}
        for item, value in self.settings.items():
            self.settings[item]
            if self.settings[item] is None:
                self.settings[item] = self.default[self.i]
            self.i += 1
        _rss.save_settings(self.settings)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("RSSticker")
    app = RSSticker(master=root)
    app.mainloop()
