import tkinter
import unittest
from unittest.mock import call, patch, PropertyMock
import webbrowser
import tkinter as tk
from tkinter import ttk
import os, sys
from tkinter import font
import queue
sys.path.append("../")
from RSS.view.userinterface import RSSticker as ui
from RSS.controller.rssfeed import RssController


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

class TestUI(unittest.TestCase):

    """Test class for RSS.view.userinterface.RSSticker."""

    _dict_newsreel = {'newsreel': [{
        'title': 'Coronavirus: UK deaths double in 24 hours',
        'title_detail': {
            'type': 'text/plain',
            'language': None,
            'base': 'http://feeds.bbci.co.uk/news/rss.xml',
            'value': 'Coronavirus: UK deaths double in 24 hours'
        },
        'summary': 'Ten more people have died after testing positive for the virus, NHS England says.',
        'summary_detail': {
            'type': 'text/html',
            'language': None,
            'base': 'http://feeds.bbci.co.uk/news/rss.xml',
            'value': 'Ten more people have died after testing positive for the virus, NHS England says.'
        },
        'links': [
            {
                'rel': 'alternate',
                'type': 'text/html',
                'href': 'https://www.bbc.co.uk/news/uk-51889957'
            }
        ],
        'link': 'https://www.bbc.co.uk/news/uk-51889957',
        'id': 'https://www.bbc.co.uk/news/uk-51889957',
        'guidislink': False,
        'published': 'Sat, 14 Mar 2020 22:51:15 GMT',
        'published_parsed': ''
    }]}

    def setUp(self):

        """ Initial set up of the the _dict_newsreel dictionary."""

        self.newsreel = Struct(**self._dict_newsreel)

    def test_show_feeds(self):

        """ Unit test for RSS.view.userinterface.RSSticker.show_feeds.
        Test to ensure that the function shows the user the feeds they have
        added to the application.
        """

        # with patch.object(ui, 'Tk') as mock:
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                app = ui(mock_controller)
                feeds = ['aFeed?Where']
                app.show_feeds(feeds)
                mock_window.assert_has_calls([
                    call().pack(side='top', fill='x', pady=10),
                ], any_order=True)

    def test_cycle_time(self):

        """ Unit test for RSS.view.userinterface.RSSticker._cycle_time.
        Test to ensure that the window shows headlines are cycled through at least
        every 5 seconds.
        """

        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                app = ui(mock_controller)
            arg0 = 5
            app.set_cycle_time(arg0)
            self.assertIsNotNone(app.time)

    def test_user_font_color(self):
        
        """ Unit test for RSS.view.userinterface.RSSticker._font_color.
        Test to ensure that the window shows headlines in the font color chosen.
        """

        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                app = ui(mock_controller)
            arg0 = 'blue'
            app.user_font_color(arg0)
            self.assertIsNotNone(app.time)

    def test_user_font_style(self):

        """ Unit test for RSS.view.userinterface.RSSticker._font_style.
        Test to ensure that the window shows headlines in the font style chosen.
        """

        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                app = ui(mock_controller)
            arg0 = 'Times'
            app.user_font_style(arg0)
            self.assertIsNotNone(app.time)

    def test_user_font_size(self):

        """ Unit test for RSS.view.userinterface.RSSticker._font_size.
        Test to ensure that the window shows headlines in the font size chosen.
        """

        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                app = ui(mock_controller)
            arg0 = 12
            app.user_font_size(arg0)
            self.assertIsNotNone(app.time)

    def test_set_font(self):

        """ Unit test for RSS.view.userinterface.RSSticker label font style.
        Test to ensure that the font if set and that there is a color,
        style, and size.
        """

        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                with patch('tkinter.font.Font', new_callable=PropertyMock) as mock_font:
                    app = ui(mock_controller)
                    color = app.font_color
                    size = app.font_size
                    style = app.font_type
                    app.set_font()
                    mock_font.assert_has_calls(mock_font.configure(size=size, family=style))
                    mock_window.assert_has_calls(mock_window.configure(font=app.user_font, foreground=color))

    def test_save(self):

        """ Unit test for view.userinterface.RSSticker.save.
        Test to ensure that the configurations of the window are saved.
        """

        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                app = ui(mock_controller)
            color = 'powder blue'
            place = 'top right'
            font_color = 'black'
            font_type = 'Times'
            font_size = 12
            feeds = ["AReallyFakeFeed", "AnEvenFakerFeed"]
            time = 30
            app.save(color, place, time, font_color, font_size, font_type, feeds)
            self.assertIsNotNone(app.settings)

    def test_backgroundcolor(self):

        """ Unit test for RSS.view.userinterface.RSSticker.background_color.
        Test to ensure that the window backgrond color can be configured.
        """

        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                app = ui(mock_controller)

            arg0 = "red"
            app.background_color(arg0)
            mock_window.assert_has_calls(mock_window.configure(background=arg0))

    def test_window_placment(self):

        """ Unit test for RSS.view.userinterface.RSSticker.window_placement.
        Test to ensure that the window can be placed on the top left and right, 
        and bottom left and right.
        """

        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                app = ui(mock_controller)
                root = mock_window.Tk()
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

    def listen_for_result_fail(self):

        """ Unit test to ensure that the the controller is trying to get the news reel. """

        with patch.object(RssController, 'next_feed', return_value=self.newsreel) as mock_window:
            with patch.object(ui, 'config', return_value=None) as mock_ctrl:
                with self.assertRaises(queue.Empty):
                    _ui = ui(RssController())
                    _ui.thread_queue.get()
                    _ui.listen_for_result()

    def test_run_newsreel(self):

        """ Unit test for RSS.view.userinterface.RSSticker.run_newsreel.
        Test to ensure that the newsreel is not empty so that the function can be run.
        """

        with patch.object(RssController, 'next_feed', return_value=self.newsreel) as mock_window:
            with patch.object(ui, 'config', return_value=None) as mock_ctrl:
                _ui = ui(RssController())
                _ui.run_newsreel()
                assert _ui.thread_queue.not_empty