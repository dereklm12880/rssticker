#https://github.com/int-thumbWar-1-2-3-4/Python-RSS-ticker/blob/development/tests/test_main_view.py
import sys
import unittest
import time
from unittest.mock import MagicMock
import tkinter as tk
from unittest.mock import patch
sys.path.append("../")
from RSS.view.userinterface import RSSticker


def test_build_window_winfo_toplevel(self):
    expected_text = 'Python RSS Ticker'

    root = tk.Tk()
    test_view = MainView(master=root)
    test_view.build_window()
    self.assertTrue(test_view.winfo_toplevel().title, expected_text)

    def test_build_window_content_label(self):
        """
        Unit test for view.main_view.Model.build_window
        (specifically the content_label feature)
        """
        with patch('view.main_view.tk.Label', new_callable=PropertyMock) as mock_label:
            root = tk.Tk()
            test_view = MainView(master=root)
            test_view.build_window()
            mock_label.assert_has_calls([
                call().__setitem__('text', '[BLANK Entry Title]'),
                call().pack(side="top"),
            ], any_order=True)

    def test_display_entry(self):
        """ Unit test for view.main_view.Model.build_window """
        fake_title = 'Man explodes'
        fake_link = 'www.virus.com'

        root = tk.Tk()
        test_view = MainView(master=root)

        test_view.display_entry(fake_title, fake_link)
        self.assertEqual(test_view.entry_title, fake_title)
        self.assertEqual(test_view.entry_link, fake_link)

        test_view.content_label = PropertyMock()
        self.assertTrue(test_view.content_label.call().__setitem__('text', fake_title))