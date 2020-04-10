import unittest
from unittest.mock import call, patch, PropertyMock
import webbrowser
import tkinter as tk
from tkinter import ttk
import os, sys
#from RSS.view.userinterface import RSSticker
sys.path.append("../")
from RSS.view import userinterface as ui

class TestUI(unittest.TestCase):
    
    def test_build_window(self):
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            root = tk.Tk()
            app = ui.RSSticker(master=root)
            app.build_window()

            mock_window.assert_has_calls([
                call().__setitem__('test', '[insert headline here]'),
                call().pack(side='top'),
            ], any_order=True)

