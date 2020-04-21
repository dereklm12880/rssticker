import tkinter
import feedparser
import webbrowser
import os
import tkinter as tk
from tkinter import ttk
from RSS.controller.rssfeed import RssController

    def help(self):
        locationsDict = {
            'top left': 'top left',
            'top right': 'top right',
            'bottom left': 'bottom left',
            'bottom right': 'bottom right'
        }

        print('move_window <location>: Specify window location', 
            ' location values: ', sep='\n')
        
        for l in locationsDict:
            print('\t', l, '\n')

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

    def move_window(self, location):
        if location == 'top left':
            window_placement('top left')
        elif location == 'top right':
            window_placement('top right')
        elif location == 'bottom left':
            window_placement('bottom left')
        elif location == 'bottom right':
            window_placement('bottom right')