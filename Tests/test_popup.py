import unittest
from unittest.mock import call, patch, PropertyMock
import webbrowser
import tkinter
import os, sys
#from RSS.view.userinterface import RSSticker
sys.path.append("../")
from RSS.view import userinterface as ui

class TestPopup(unittest.TestCase):
    def setUp(self):
        self.view = ui.RSSticker()
    
    def test_build_window(self):
        with patch("tkinter.Window", new_callable=PropertyMock) as mock_window:
            root = tkinter.Tk()
            app = self.view(master=root)
            app.build_window()

            mock_window.assert_has_calls([
                call().__setitem__('test', '[insert headline here]'),
                call().pack(side='top'),
            ], any_order=True)
