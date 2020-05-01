import unittest
from unittest.mock import call, patch, PropertyMock
import webbrowser
import tkinter as tk
from tkinter import ttk
import os, sys

sys.path.append("../")
from RSS.view import userinterface as ui


class TestUI(unittest.TestCase):

    """Test class for RSS.view.userinterface.RSSticker."""

    # https://github.com/drsjb80/MockingPython/blob/master/mocktk.py
    def test_build_window(self):
        """ Unit test for RSS.view.userinterface.RSSticker.build_window.
        Test to build the window is on the top left corner of the screen.
        """
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            root = mock_window.Tk()
            app = ui.RSSticker(master=root)
            app.build_window()
            mock_window.assert_has_calls([
                call().pack(side='top'),
            ], any_order=True)

    def test_refresh(self):
        """ Unit test for RSS.view.userinterface.RSSticker.refresh.
        Test to refresh the cycled headlines and URLs, and open in
        a new browser window.
        """
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            root = mock_window.Tk()
            app = ui.RSSticker(master=root)
            headline = 'Google'
            link = 'www.google.com'
            app.refresh(headline, link)
            mock_window.assert_has_calls(mock_window.configure('Google'),
                                         mock_window.bind("<Button-1", lambda e: webbrowser.open_new('www.google.com')))
    
    def test_cycle_time(self):
        """ Unit test for RSS.view.userinterface.RSSticker.cycle_time.
        Test to ensure that the window shows headlines as they are cycled
        through instead of showing only one headline.
        """
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            root = mock_window.Tk()
            app = ui.RSSticker(master=root)
            arg0 = 5
            app.cycle_time(arg0)
            self.assertIsNotNone(app.time)

    def test_backgroundcolor(self):
        """ Unit test for RSS.view.userinterface.RSSticker.background_color.
        Test to ensure that the window backgrond color can be configured.
        """
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            root = mock_window.Tk()
            app = ui.RSSticker(master=root)
            arg0 = "red"
            app.background_color(arg0)
            mock_window.assert_has_calls(mock_window.configure(background=arg0))

    def test_window_placment(self):
        """ Unit test for RSS.view.userinterface.RSSticker.window_placement.
        Test to ensure that the window can be placed on the top left and right, 
        and bottom left and right.
        """
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            root = mock_window.Tk()
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
