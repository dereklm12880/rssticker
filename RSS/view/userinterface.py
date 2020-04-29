# references: https://www.youtube.com/watch?v=HxU_5LvkVrw
# references: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/fonts.html
import tkinter
import feedparser
import webbrowser
import tkinter as tk
from tkinter import ttk
<<<<<<< HEAD
from tkinter import simpledialog
from tkinter import font
from RSS.controller.rssfeed import RssController


class RSSticker(tk.Frame):
    font_color = 'black'
    font_size = 12
    font_type = 'Times'
    time = 5
    place = 'top Left'
    color = 'white'
    feeds = []
    input = ""
    headline = "some article"
    link = "https://www.bbc.co.uk/news/world-us-canada-52428994"
=======
import os, sys
sys.path.append("../")
from RSS.controller import rssfeed as controller


class RSSticker(tk.Frame):
    time = None
    place = None
    color = None
>>>>>>> feature/eesha

    def __init__(self, master=None):
        super().__init__(master)
        self.settings = {}
        self.user_font = None
        self.T = tk.Text(self, font=("bold", 32,))
        self.master = master
        self.popup_window = ttk.Label(master)
        self.build_window()
        self.build_menu()
        self.refresh(RSSticker.headline, RSSticker.link)
        self.pack()

    def build_window(self):
        self.popup_window.pack(side="top")

    def refresh(self, headline, link):
        print("headline:", headline, "\nlink:", link)
        self.popup_window.configure(text=headline)
        self.popup_window.bind("<Button-1>", lambda e: webbrowser.open_new(link))

    def build_menu(self):
        menu_bar = tk.Menu(self.popup_window)
        dropdown_menu = tk.Menu(menu_bar)
        color_menu = tk.Menu(dropdown_menu)
        placement_menu = tk.Menu(dropdown_menu)
        cycle_time_menu = tk.Menu(dropdown_menu)
        font_menu = tk.Menu(dropdown_menu)
        font_colors_menu = tk.Menu(font_menu)
        font_families_menu = tk.Menu(font_menu)
        font_size_menu = tk.Menu(font_menu)
        feed_menu = tk.Menu(dropdown_menu)
        list_colors = ["powder blue", "gray", "light green", "white"]
        list_placement = ["top left", "bottom left", "top right", "bottom right"]
        cycle_options = [5, 10, 15, 20, 25, 30]
        font_colors = ['blue', 'black', 'red', 'magenta']
        font_types = ['Times', 'Helvetica', 'Arial', 'Candara', 'Futara', 'Courier']
        font_sizes = [11, 12, 14, 16, 18, 20, 22, 24]
        feed_menu.add_radiobutton(label="show feeds", command=lambda: RSSticker.show_feeds(self, self.feeds))
        feed_menu.add_command(label="add feeds", command=lambda: RSSticker.add_feeds(self))
        for style in font_types:
            font_families_menu.add_radiobutton(label=style,
                                               command=lambda arg0=style: RSSticker.user_font_style(self, arg0))
        for size in font_sizes:
            font_size_menu.add_radiobutton(label=size, command=lambda arg0=size: RSSticker.user_font_size(self, arg0))
        for c in font_colors:
            font_colors_menu.add_radiobutton(label=c, command=lambda arg0=c: RSSticker.user_font_color(self, arg0))
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
        font_menu.add_cascade(label="font color", menu=font_colors_menu)
        font_menu.add_cascade(label="font type", menu=font_families_menu)
        font_menu.add_cascade(label="font size", menu=font_size_menu)
        font_menu.add_radiobutton(label="Set font",
                                  command=lambda: RSSticker.set_font(self))
        dropdown_menu.add_cascade(label="Feeds", menu=feed_menu)
        menu_bar.add_cascade(label="Settings", menu=dropdown_menu)
<<<<<<< HEAD
        dropdown_menu.add_radiobutton(label="Save Settings and Feeds",
                                      command=lambda: RSSticker.save(self, RSSticker.color,
                                                                     RSSticker.place, RSSticker.time,
                                                                     RSSticker.font_size, RSSticker.font_color,
                                                                     RSSticker.font_type, RSSticker.feeds))
=======
        dropdown_menu.add_radiobutton(label="Save Settings",
                                      command=lambda: RSSticker.save(self, {'color': RSSticker.color},
                                                                     {'place': RSSticker.place},
                                                                     {'time': RSSticker.time}))
>>>>>>> feature/eesha
        self.master.config(menu=menu_bar)

    def background_color(self, arg0):
        RSSticker.color = arg0
        self.master.configure(background=arg0)

    def cycle_time(self, arg0):
        RSSticker.time = arg0
<<<<<<< HEAD
=======
        pass
>>>>>>> feature/eesha

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

<<<<<<< HEAD
    def user_font_color(self, color):
        RSSticker.font_color = color

    def user_font_style(self, style):
        RSSticker.font_type = style

    def user_font_size(self, size):
        RSSticker.font_size = size

    def set_font(self):
        font_color = RSSticker.font_color
        size = RSSticker.font_size
        style = RSSticker.font_type
        self.user_font = font.Font(size=size, family=style)
        self.popup_window.configure(font=self.user_font, foreground=font_color)

    def save(self, color, place, time, font_color, font_size, font_type, feeds):
        self.settings = {'background_color': color, 'window placement': place, 'cycle_time': time,
                         'font_color': font_color, 'font_size': font_size, 'font_type': font_type, 'feeds': feeds}
        _rss = RssController()
        _rss.save_settings(self.settings)

    def add_feeds(self):  # pragma: no cover
        self.input = simpledialog.askstring("input", "Please insert a news feed")
        if self.input != "":
            RSSticker.feeds.append(self.input)

    def show_feeds(self, feeds):
        popup = tk.Tk()
        popup.geometry("200x50")
        popup.wm_title("Feeds")
        label = ttk.Label(popup, text=feeds)
        label.pack(side="top", fill="x", pady=10)
        popup.mainloop()

# Just temporary,for viewing purposes
if __name__ == "__main__":
    root = tk.Tk()
    root.title("RSSticker")
    app = RSSticker(master=root)
    app.mainloop()
=======
    def save(self, color, place, time):
        settings = [color, place, time]
        controller.RssController.save_settings(settings)
        print(time)
        print(place)
        print(color)
        pass
>>>>>>> feature/eesha
