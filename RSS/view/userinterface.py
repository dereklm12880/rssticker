# references: https://www.youtube.com/watch?v=HxU_5LvkVrw
# references: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/fonts.html
# https://scorython.wordpress.com/2016/06/27/multithreading-with-tkinter/
import tkinter
import feedparser
import webbrowser
import os
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import font
import multiprocessing.dummy as mp
import threading
import queue
import time
import webbrowser



def update_feed(thread_queue):
    """
    After result is produced put it in queue
    """
    result = 0
    for i in range(1000):
        # Do something with result
        result = result + 1
    thread_queue.put(result)


class RSSticker(tk.Tk):
    font_color = 'black'
    font_size = 12
    font_type = 'Times'
    _default_cycle_time = 5
    place = 'top Left'
    color = 'white'
    feeds = []
    input = ""
    _rss = None
    app_title = "RSS Ticker"
    _tk = None
    T = None
    user_font = None
    settings = {}
    width = 500
    height = 300
    ctrl = None

    def __init__(self, ctrl):
        self.ctrl = ctrl
        ####### Do something ######
        super(RSSticker, self).__init__()
        self.myframe = tk.Frame(self)
        self.myframe.grid(row=0, column=0, sticky='nswe')
        self.mylabel = tk.Label(self.myframe)  # Element to be updated
        self.mylabel.config(text='No feeds given', anchor=tk.CENTER)
        self.mylabel.grid(row=0, column=0)
        self.desc = tk.Label(self.myframe)
        self.desc.config(text='', anchor=tk.CENTER)
        self.desc.grid(row=1, column=0)

        self.next = tk.Button(
            self.myframe,
            text='Next Feed',
            command=lambda: self.get_feed)
        self.next.grid(row=3, column=0)

        self.geometry("{}x{}".format(self.width, self.height))
        self.title(self.app_title)

    def run_newsreel(self):
        """
        Spawn a new thread for running long loops in background
        """
        self.mylabel.config(text='Getting next feed')
        print('Getting Next Feed')

        # self.thread_queue = queue.Queue()
        """ 
        TODO Consider using kwargs and queue threads for updating settings at 
        runtime--TODO TODO: see if that is even possible.
        """
        self.new_thread = threading.Thread(
            target=self.get_feed
            # ,kwargs={
            #     'thread_queue': self.thread_queue
            # }
        )
        self.new_thread.start()
        # self.after(10000, self.run_newsreel)

    # def get_feed(self, thread_queue):
    """
    This is a threaded method and should not impact the user experience while 
    cycling through feeds.
    """
    def get_feed(self):
        while True:
            try:
                _next_feed = self.ctrl.next_feed()
                # thread_queue.put(_next_feed)
                for feed in _next_feed.newsreel:
                    self.desc.config(text=self.format_desc(feed), wraplength=self.width)
                    self.mylabel.config(text=feed.title, fg="blue", cursor="hand2")
                    self.mylabel.bind("<Button-1>", lambda e: webbrowser.open_new(feed.link))
                    """ User setting cycle time """
                    _t = self.ctrl.settings_model.settings['cycle_time'] \
                        if 'cycle_time' in self.ctrl.settings_model.settings \
                        else self._default_cycle_time
                    # self.refresh()
                    time.sleep(_t)
            except Exception as e:
                print(e)

        # self.refresh(_next_feed.headline, _next_feed.link)
        # self.master.mainloop()

    def format_desc(self, feed):
        _desc = feed['summary'] if 'summary' in feed else ''
        if _desc:
            """ BEAUTIFY IT """
            pass

        return _desc

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
            cycle_time_menu.add_radiobutton(
                label=time,
                command=lambda arg0=time: RSSticker.cycle_time(self, arg0)
            )
        for place in list_placement:
            placement_menu.add_radiobutton(
                label=place,
                command=lambda arg0=place: RSSticker.window_placement(self, arg0)
            )
        dropdown_menu.add_cascade(label="Cycle Time", menu=cycle_time_menu)
        dropdown_menu.add_cascade(label="Window Placement", menu=placement_menu)
        dropdown_menu.add_cascade(label="Change Background Color", menu=color_menu)
        dropdown_menu.add_cascade(label="Change Font", menu=font_menu)
        font_menu.add_cascade(label="font color", menu=font_colors_menu)
        font_menu.add_cascade(label="font type", menu=font_families_menu)
        font_menu.add_cascade(label="font size", menu=font_size_menu)
        font_menu.add_radiobutton(
            label="Set font",
            command=lambda: RSSticker.set_font(self)
        )
        dropdown_menu.add_cascade(label="Feeds", menu=feed_menu)
        menu_bar.add_cascade(label="Settings", menu=dropdown_menu)
        dropdown_menu.add_radiobutton(
            label="Save Settings and Feeds",
            command=lambda: RSSticker.save(
                self,
                RSSticker.color,
                RSSticker.place, RSSticker.time,
                RSSticker.font_size, RSSticker.font_color,
                RSSticker.font_type, RSSticker.feeds
            )
        )

        self.master.config(menu=menu_bar)

    def background_color(self, arg0):
        RSSticker.color = arg0
        self.master.configure(background=arg0)

    def set_cycle_time(self, time):
        RSSticker.time = time

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
        self.ctrl.save_settings(self.settings)

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

    def run(self):
        self.build_window()
        self.build_menu()
        self.pack()
        self.master.mainloop()
