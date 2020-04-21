import tkinter
import feedparser
import webbrowser
import os
import tkinter as tk
from tkinter import ttk
from RSS.controller.rssfeed import RssController
from RSS.view.userinterface import RSSticker

class CommandLineInputs:
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

    def move_window(self, location):
        if location == 'top left':
            view.window_placement('top left')
        elif location == 'top right':
            view.window_placement('top right')
        elif location == 'bottom left':
            view.window_placement('bottom left')
        elif location == 'bottom right':
            view.window_placement('bottom right')