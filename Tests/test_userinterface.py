import unittest
from unittest.mock import call, patch, PropertyMock
import webbrowser
import tkinter as tk
from tkinter import ttk
import os, sys
sys.path.append("../")
from RSS.view import userinterface as ui

class TestUI(unittest.TestCase):


    def test_start(self):
        """Checks functionality of .mainloop()"""
        with patch('RSS.view.userinterface.tk.Tk') as mock_window:
            root = tk.Tk()
            app = ui.RSSticker(master=root)
            app.start()
            mock_window.assert_has_calls(mock_window.mainloop())

    #https://github.com/drsjb80/MockingPython/blob/master/mocktk.py
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

            mock_window.assert_has_calls([
              # dropdown menus have "powder blue", "gray", "light green", "white" options
            ])

    def test_background_color(self):
        arg0 = "red"
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            mock_window.assert_has_calls(mock_window.config(arg0))
