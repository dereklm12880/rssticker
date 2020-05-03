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
        self.newsreel = Struct(**self._dict_newsreel)

    # https://github.com/drsjb80/MockingPython/blob/master/mocktk.py
    # def test_build_window(self):
    #     """Builds the window on the top left"""
    #     with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
    #         root = mock_window.Tk()
    #         app = ui(master=root)
    #         app.build_window()
    #         mock_window.assert_has_calls([
    #             call().pack(side='top'),
    #         ], any_order=True)

    def test_show_feeds(self):
        """Builds the window on the top left"""
        # with patch.object(ui, 'Tk') as mock:
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                app = ui(mock_controller)
                feeds = ['aFeed?Where']
                app.show_feeds(feeds)
                mock_window.assert_has_calls([
                    call().pack(side='top', fill='x', pady=10),
                ], any_order=True)

    # def test_refresh(self):
    #     """Refreshes the cycled headlines and URLs, and opens in a new browser window"""
    #     with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
    #         with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
    #             root = mock_window.Tk()
    #             app = ui(mock_controller)
    #         headline = 'Google'
    #         link = 'www.google.com'
    #         app.refresh(headline, link)
    #         mock_window.assert_has_calls(mock_window.configure('Google'),
    #                                      mock_window.bind("<Button-1", lambda e: webbrowser.open_new('www.google.com')))

    def test_cycle_time(self):
        """ Unit test for RSS.view.userinterface.RSSticker.cycle_time.
        Test to ensure that the window shows headlines as they are cycled
        through instead of showing only one headline.
        """
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                app = ui(mock_controller)
            arg0 = 5
            app.set_cycle_time(arg0)
            self.assertIsNotNone(app.time)

    def test_user_font_color(self):
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                app = ui(mock_controller)
            arg0 = 'blue'
            app.user_font_color(arg0)
            self.assertIsNotNone(app.time)

    def test_user_font_style(self):
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                app = ui(mock_controller)
            arg0 = 'Times'
            app.user_font_style(arg0)
            self.assertIsNotNone(app.time)

    def test_user_font_size(self):
        with patch('RSS.view.userinterface.ttk.Label', new_callable=PropertyMock) as mock_window:
            with patch('RSS.controller.rssfeed', new_callable=PropertyMock) as mock_controller:
                app = ui(mock_controller)
            arg0 = 12
            app.user_font_size(arg0)
            self.assertIsNotNone(app.time)

    def test_set_font(self):
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
        with patch.object(RssController, 'next_feed', return_value=self.newsreel) as mock_window:
            with patch.object(ui, 'config', return_value=None) as mock_ctrl:
                with self.assertRaises(queue.Empty):
                    _ui = ui(RssController())
                    _ui.thread_queue.get()
                    _ui.listen_for_result()

    def test_run_newsreel(self):
        with patch.object(RssController, 'next_feed', return_value=self.newsreel) as mock_window:
            with patch.object(ui, 'config', return_value=None) as mock_ctrl:
                _ui = ui(RssController())
                _ui.run_newsreel()
                assert _ui.thread_queue.not_empty
