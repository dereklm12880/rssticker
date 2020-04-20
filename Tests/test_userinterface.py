import unittest
from unittest.mock import call, patch, PropertyMock
import webbrowser
import tkinter as tk
from tkinter import ttk
import os, sys

sys.path.append("../")
from RSS.view import userinterface as ui


class TestUI(unittest.TestCase):

    # https://github.com/drsjb80/MockingPython/blob/master/mocktk.py
    def test_build_window(self):
        """Builds the window on the top left"""
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            root = tk.Tk()
            app = ui.RSSticker(master=root)
            app.build_window()
            mock_window.assert_has_calls([
                call().pack(side='top'),
            ], any_order=True)

    def test_refresh(self):
        """Refreshes the cycled headlines and URLs, and opens in a new browser window"""
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            root = tk.Tk()
            app = ui.RSSticker(master=root)
            headline = 'Google'
            link = 'www.google.com'
            app.refresh(headline, link)
            mock_window.assert_has_calls(mock_window.configure('Google'),
                                         mock_window.bind("<Button-1", lambda e: webbrowser.open_new('www.google.com')))
    
    def test_build_menu(self):
        with patch('RSS.view.userinterface.tk.Menu', new_callable=PropertyMock) as mock_window:
            root = tk.Tk()
            app = ui.RSSticker(master=root)
            app.build_menu()

            list_colors = ['powder blue', 'gray', 'light green', 'white']
            list_placement = ['top left', 'bottom left', 'top right', 'bottom right']
            cycle_options = [5, 10, 15, 20, 25, 30]
            
            for color in list_colors:
                mock_window.assert_has_calls(root.add_radiobutton(label=color, command=lambda arg0=color: RSSticker.background_color(self, arg0))
            
            for time in cycle_options:
                mock_window.assert_has_calls(root.add_radiobutton(label=time, command=lambda arg0=time: RSSticker.cycle_time(self, arg0))
            
            for place in list_placement:
                mock_window.assert_has_calls(root.add_radiobutton(label=place,
                                           command=lambda arg0=place: RSSticker.window_placement(self, arg0))

        self.menu_bar.add_cascade(label="Cycle Time", menu=cycle_time_menu)
        self.menu_bar.add_cascade(label="Window Placement", menu=placement_menu)
        self.menu_bar.add_cascade(label="Change Background Color", menu=color_menu)
        self.menu_bar.add_cascade(label="Settings", menu=self.menu_bar)
        self.menu_bar.add_command(label="Save Settings", command=RSSticker.save())
        # self.master.config(menu=menu_bar)
            #mock_window.assert_has_calls([
              # dropdown menus have "powder blue", "gray", "light green", "white" options
            #])

    def test_background_color(self):
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            root = tk.Tk()
            app = ui.RSSticker(master=root)
            arg0 = "red"
            app.background_color(arg0)
            mock_window.assert_has_calls(mock_window.configure(background=arg0))
    
    def test_cycle_time(self):
        with patch('RSS.view.userinterface.', new_callable=PropertyMock) as mock_window:
            root = tk.Tk()
            app = ui.RSSticker(master=root)
            app.cyle_time()

    def test_window_placment(self):
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            root = tk.Tk()
            app = ui.RSSticker(master=root)
            list_placement = ["top left", "bottom left", "top right", "bottom right"]
            for place in list_placement:
                app.window_placement(place)
                if place == 'top left':
                    mock_window.assert_has_calls(root.geometry("+0+0"))
                elif place == "bottom left":
                    mock_window.assert_has_calls(root.geometry("+0+750"))
                elif place == "top right":
                    mock_window.assert_has_calls(root.geometry("+1000+0"))
                elif place == "bottom right":
                    mock_window.assert_has_calls(root.geometry("+1000+750"))

    def test_save(self):
        with patch('RSS.view.userinterface.', new_callable=PropertyMock) as mock_window:
            root = tk.Tk()
            app = ui.RSSticker(master=root)
            app.save()