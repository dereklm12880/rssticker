# references: https://www.youtube.com/watch?v=HxU_5LvkVrw
import tkinter
import feedparser
import webbrowser
import os, sys
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import font
sys.path.append("../")
from RSS.model.rssfeed import RssModel
from RSS.controller.rssfeed import RssController


class RSSticker(tk.Frame):

    """ Class view.userinterface.RSSticker.
    This class customizes the Tkinter root window. It creates, displays, modifies
    and receives input from the controller.
    """

    font_color = None
    font_size = None
    font_type = None
    time = None
    place = None
    color = None
    feeds = []
    input = ""
    _rss = None

    def __init__(self, master=None):

        """Constructor for view.userinterface.RSSticker."""

        super().__init__(master)
        self.settings = {}
        self.T = tk.Text(self, font=("bold", 32,))
        self.master = master
        self.popup_window = ttk.Label(master)
        self.build_window()
        self.build_menu()
        self.pack()

    def start(self):

        """ Function view.userinterface.RSSticker.start.
        This function serves to call the controller for later use.
        """

        try:
            self._rss = RssController()
        except Exception as e:
            print(e)
    
    def get_feed(self):

        """ Function view.userinterface.RSSticker.get_feed.
        This function serves to retrieve the headlie and link for the RSS feeds
        that have been parsed and cycled through in the controller.
        """

        _next_feed = self._rss.next_feed()
        self.refresh(_next_feed.headline, _next_feed.link)
        self.master.mainloop()

    def build_window(self):

        """ Function view.userinterface.RSSticker.build_window.
        This function build the window in the top left of the screen as a default.
        """

        self.popup_window.pack(side="top")

    def refresh(self, headline, link):

        """ Function view.userinterface.RSSticker.refresh.
        This function serves to configure the size of the font of
        the text that is passed in this window.
        Arguments:
        headline -- the headline that appears on the window.
        link -- the clickable link that opens the article in a webbrowser.
        """

        print("headline:", headline, "\nlink:", link)
        self.popup_window.configure(text=headline)
        self.popup_window.bind("<Button-1>", lambda e: webbrowser.open_new(link))

    def build_menu(self):

        """ Function view.userinterface.RSSticker.build_menu.
        This function adds a drop down menu for the Tkinter root window. When
        the application is launched, the menu appears inside the window (Windows OS)
        or on the menu bar (MacOS). It also assigns a lambda function to 
        each of the dropdown menu's options.
        """

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
        font_types = ['Times', 'Helvetica', 'Arial']
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
                                  command=lambda: RSSticker.set_font(self, RSSticker.font_type, RSSticker.font_size,
                                                                     RSSticker.font_color))
        dropdown_menu.add_cascade(label="Feeds", menu=feed_menu)
        menu_bar.add_cascade(label="Settings", menu=dropdown_menu)
        dropdown_menu.add_radiobutton(label="Save Settings and Feeds",
                                      command=lambda: RSSticker.save(self, RSSticker.color,
                                                                     RSSticker.place, RSSticker.time,
                                                                     RSSticker.font_size, RSSticker.font_color,
                                                                     RSSticker.font_type, RSSticker.feeds))
        self.master.config(menu=menu_bar)

    def background_color(self, arg0):

        """ Function view.userinterface.RSSticker.background_color.
        This function serves to configure the background of this window.
        Arguments:
        arg0 -- an argument the sets the color.
        """

        RSSticker.color = arg0
        self.master.configure(background=arg0)

    def cycle_time(self, arg0):

        """ Function view.userinterface.RSSticker.cycle_time.
        This function serves to configure the cycle time of the headlines
        that are passed through this window.
        Arguments:
        arg0 -- an argument the sets the cycle time.
        """

        RSSticker.time = arg0

    def window_placement(self, arg0):

        """ Function view.userinterface.RSSticker.window_placement.
        This function serves to configure the placement of this window on the user's screen.
        Arguments:
        arg0 -- an argument the sets the placement of the window.
        """

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

        """ Function view.userinterface.RSSticker.user_font_color.
        This function serves to configure the font color of the text
        that is passed in this window.
        Arguments:
        color -- an argument the sets the color of the font.
        """

        RSSticker.font_color = color

    def user_font_style(self, style):
        """ Function view.userinterface.RSSticker.user_font_style.
        This function serves to configure the font style of the text
        that is passed in this window.
        Arguments:
        style -- an argument the sets the style of the font.
        """
        RSSticker.font_type = style

    def user_font_size(self, size):

        """ Function view.userinterface.RSSticker.user_font_size.
        This function serves to configure the size of the text
        that is passed in this window.
        Arguments:
        size -- an argument the sets the font size.
        """

        RSSticker.font_size = size

    def set_font(self, font_color, font_type, font_size):

        """ Function view.userinterface.RSSticker.set_font.
        This function serves to configure the size of the font of
        the text that is passed in this window.
        Arguments:
        font_color -- an argument the sets the font color.
        font_type -- an argument the sets the font type.
        font_size -- an argument the sets the font size.
        """

        font_color = RSSticker.font_color
        font_type = RSSticker.font_type
        font_size = RSSticker.font_size
        user_font = font.Font(family=font_type, size=font_size)
        self.popup_window.configure(font=user_font, foreground=font_color)

    def save(self, color, place, time, font_color, font_size, font_type, feeds):

        """ Function view.userinterface.RSSticker.save.
        This function serves to save the configurations of the window
        once set.
        Arguments:
        color -- argument for storing the background color.
        place -- argument for storing the window placement.
        time -- argument for the storing cycle time.
        font_color -- argument for storing the font color.
        font_size -- argument for storing the font size.
        font_type -- argument for storing the font type.
        feeds -- argument for storing the feeds.
        """

        self.settings = {'background_color': color, 'window placement': place, 'cycle_time': time,
                         'font_color': font_color, 'font_size': font_size, 'font_type': font_type, 'feeds': feeds}
        _rss = RssController()
        _rss.save_settings(self.settings)

    def add_feeds(self):  # pragma: no cover

        """ Function view.userinterface.RSSticker.add_feeds.
        This function prompts the user to insert a news feed and apped it. If they
        haven't, an exception will be thrown.
        """

        self.input = simpledialog.askstring("input", "Please insert a news feed")
        if self.input != "":
            try:
                RSSticker.feeds.append(self.input)
            except Exception as e:
                print(e)

    def show_feeds(self, feeds):

        """ Function view.userinterface.RSSticker.show_feeds.
        This function shows the user the feeds they have added to the application.
        """
        
        popup = tk.Tk()
        popup.geometry("200x50")
        popup.wm_title("Feeds")
        label = ttk.Label(popup, text=feeds)
        label.pack(side="top", fill="x", pady=10)
        popup.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("200x50")
    root.title("RSSticker")
    app = RSSticker(master=root)
    app.mainloop()