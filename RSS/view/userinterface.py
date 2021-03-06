# references: https://www.youtube.com/watch?v=HxU_5LvkVrw
# references: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/fonts.html
# https://scorython.wordpress.com/2016/06/27/multithreading-with-tkinter/

import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import font
import threading
import queue
import webbrowser

def update_feed(thread_queue, feed):

    """ Function view.userinterface.update_feed.
    This function updates the feed with the threaded queue.
    Arguments:
    thread_queue -- an argument for the threaded feeds in the news reel.
    feed -- an argument for the feeds.
    """
    
    for news in feed.newsreel:
        thread_queue.put(news)
    # Think of the RSSticker as extending the Tkinter object.

class RSSticker(tk.Tk):

    """ Class view.userinterface.RSSticker.
    This class customizes the Tkinter root window. It creates, displays, modifies
    and receives input from the controller.
    """

    font_color = 'black'
    font_size = 12
    font_type = 'Times'
    _default_cycle_time = 5
    place = 'top Left'
    color = None
    feeds = ["https://www.reddit.com/r/worldnews/.rss"]
    time = 5
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

        """Constructor for view.userinterface.RSSticker."""

        self.ctrl = ctrl
        super(RSSticker, self).__init__()
        self.feed_frame = tk.Frame(self)
        self.feed_frame.grid(row=1, column=0, sticky='we')
        self.feed_title = tk.Label(self.feed_frame)  # Element to be updated
        self.feed_title.config(text='No feeds given', anchor=tk.CENTER)
        self.feed_title.grid(row=1, column=0)
        self.thread_queue = queue.Queue()
        self.next = tk.Button(
            self.feed_frame,
            text='Next Feed',
            command=self.next_newsreel)
        self.next.grid(row=0, column=0)
        self.grid_columnconfigure(1, weight=1)
        self.geometry("{}x{}".format(self.width, self.height))
        self.title(self.app_title)
        self._background_color()
        self._font_color()
        self.build_menu()
        self.feed_frame.pack()
        self.window_placement(self.ctrl.settings_model.settings['window_placement'] or self.place)
        self.user_font_size(self.ctrl.settings_model.settings['font_size'] or self.font_size)
        self.user_font_style(self.ctrl.settings_model.settings['font_type'] or self.font_type)

    def run_newsreel(self):

        """ Function view.userinterface.RSSticker.run_newsreel.
        This function uses threading to get the get the next feeds.
        """

        self.feed_title.config(text='Getting next feed')

        """ 
        TODO: Consider using kwargs and queue threads for updating settings at 
        runtime-
        TODO: see if that is even possible.
        """

        try:
            if self.thread_queue.empty():
                _next_feed = self.ctrl.next_feed()
                self.new_thread = threading.Thread(
                    target=update_feed
                    , kwargs={
                        'thread_queue': self.thread_queue,
                        'feed': _next_feed
                    }
                )
                self.new_thread.start()
            self.after(100, self.listen_for_result)
        except Exception as e:
            print(e)

    # def get_feed(self, thread_queue):
    """
    This is a threaded method and should not impact the user experience while 
    cycling through feeds.
    """

    def listen_for_result(self):   # pragma: no cover

        """ Function view.userinterface.RSSticker.listen_for_result.
        This function checks to see if there's something in the queue of
        _newsreel and runs it once the queue is empty.
        """

        try:
            _newsreel = self.thread_queue.get()
            self._update_view(_newsreel.title, _newsreel.link)
            self.after(1000 * self._cycle_time(), self.listen_for_result)
        except queue.Empty:
            self.run_newsreel()

    def next_newsreel(self):  # pragma: no cover

        """ Function view.userinterface.RSSticker.next_newsreel.
        This function gets the next _newsreel and runs it once the queue is empty.
        """

        try:
            _newsreel = self.thread_queue.get()
            self._update_view(_newsreel.title, _newsreel.link)
        except queue.Empty as e:
            self.run_newsreel()

    def _update_view(self, title, link):

        """ Function view.userinterface.RSSticker._update_view.
        This function updates what the window with the headline and allows
        you to open up the link on a new browser window.
        Arguments:
        title -- the headline that appears on the window.
        link -- the clickable link that opens the article in a webbrowser.
        """

        self.feed_title.config(text=title, wraplength=self.width, cursor="hand2")
        self.feed_title.bind("<Button-1>", lambda e: webbrowser.open_new(link))

    def _cycle_time(self):

        """ Function view.userinterface.RSSticker._cycle_time.
        This function returns the cycle time determined in the settings model,
        or the default cycle time.
        """

        return self.ctrl.settings_model.settings['cycle_time'] \
            if 'cycle_time' in self.ctrl.settings_model.settings \
            else self._default_cycle_time

    def _background_color(self):

        """ Function view.userinterface.RSSticker._background_color.
        This function returns the background color determined in the settings model,
        or the default bacground color.
        """

        return self.ctrl.settings_model.settings['background_color'] \
            if 'cycle_time' in self.ctrl.settings_model.settings \
            else self.color

    def build_menu(self):

        """ Function view.userinterface.RSSticker.build_menu.
        This function adds a drop down menu for the Tkinter root window. When
        the application is launched, the menu appears inside the window (Windows OS)
        or on the menu bar (MacOS). It also assigns a lambda function to 
        each of the dropdown menu's options.
        """

        menu_bar = tk.Menu(self.feed_frame)
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
                command=lambda arg0=time: RSSticker.set_cycle_time(self, arg0)
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

        self.config(menu=menu_bar)

    def background_color(self, arg0):  

        """ Function view.userinterface.RSSticker.background_color.
        This function serves to configure the background of this window.
        Arguments:
        arg0 -- an argument the sets the color.
        """

        RSSticker.color = arg0
        self.configure(background=arg0)
        self.feed_title.configure(background=arg0)
        
    def _font_color(self):

        """ Function view.userinterface.RSSticker._font_color.
        This function returns the font color determined in the settings model,
        or the default font color.
        """

        return self.ctrl.settings_model.settings['font_color'] \
            if 'font_color' in self.ctrl.settings_model.settings \
            else self.font_color

    def set_cycle_time(self, time):

        """ Function view.userinterface.RSSticker.set_cycle_time.
        This function serves to configure the cycle time for the headlines to refresh.
        Arguments:
        time -- an argument the sets the cycle time.
        """

        RSSticker.time = time

    def window_placement(self, arg0):  

        """ Function view.userinterface.RSSticker.window_placement.
        This function serves to configure the placement of this window on the user's screen.
        Arguments:
        arg0 -- an argument the sets the placement of the window.
        """

        RSSticker.place = arg0
        if arg0 == "top left":
            self.geometry("+0+0")
        elif arg0 == "bottom left":
            self.geometry("+0+750")
        elif arg0 == "top right":
            self.geometry("+1000+0")
        elif arg0 == "bottom right":
            self.geometry("+1000+750")

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
        size - an argument that sets the font size.
        """

        RSSticker.font_size = size

    def set_font(self):

        """ Function view.userinterface.RSSticker.set_font.
        This function serves to configure the size of the font of
        the text that is passed in this window.
        """

        font_color = RSSticker.font_color
        size = RSSticker.font_size
        style = RSSticker.font_type
        self.user_font = font.Font(self, size=size, family=style)
        self.feed_title.configure(font=self.user_font, foreground=font_color)

    def save(self, color, place, time, font_color, font_size, font_type, feeds):

        """ Function view.userinterface.RSSticker.save.
        This function serves to save the configurations of the window
        once set.
        Arguments:
        color -- argument for setting the background color.
        place -- argument for setting the window placement.
        time -- argument for the setting cycle time.
        font_color -- argument for setting the font color.
        font_size -- argument for setting the font size.
        font_type -- argument for setting the font type.
        feeds -- argument for setting the feeds.
        """
    
        self.settings = {'background_color': color, 'window_placement': place, 'cycle_time': time,
                         'font_color': font_color, 'font_size': font_size, 'font_type': font_type, 'feeds': feeds}
        self.ctrl.save_settings(self.settings)

    def add_feeds(self):  

        """ Function view.userinterface.RSSticker.add_feeds.
        This function prompts the user to insert a news feed and if it's not an empyt string, 
        the feed is appended.
        """

        self.input = simpledialog.askstring("input", "Please insert a news feed", parent=self)
        if self.input != "":
            RSSticker.feeds.append(self.input)

    def show_feeds(self, feeds):
        
        """ Function view.userinterface.RSSticker.show_feeds.
        This function shows the user the feeds they have added to the application.
        Arguments:
        feeds -- the feeds that are being displayed in the label
        """

        popup = tk.Tk()
        popup.geometry("200x50")
        popup.wm_title("Feeds")
        label = ttk.Label(popup, text=feeds)
        label.pack(side="top", fill="x", pady=10)
        popup.mainloop()  
