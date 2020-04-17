# https://ongspxm.github.io/blog/2016/11/assertraises-testing-for-errors-in-unittest/
import os
import unittest
from unittest import mock
from unittest.mock import patch, Mock

import feedparser
import yaml

from RSS.controller.rssfeed import RssController
from RSS.model.rssfeed import RssModel
from RSS.model.settings import SettingsModel

import unittest
from unittest.mock import call, patch, PropertyMock
import webbrowser
import tkinter as tk
from tkinter import ttk
import os, sys

sys.path.append("../")
from RSS.view import userinterface as ui

import unittest
from mock import patch
from RSS.model.rssfeed import RssModel
import feedparser


class TestRssModel(unittest.TestCase):
    _return_value = {"feeds": ["http://fakefeed.com", "http://anotherfakefeed.com"]}
    _mock_open = mock.mock_open(read_data='')
    _return_value_null = {}

    def setUp(self):
        self.rss = RssModel()
        self.view = Mock()
        self.ctr = RssController()
        self.rss_url_list = None
        self.loaded_urls = ['http://fake.com', 'http://anotherfake.com']
        self.load_feed_url = ['https://www.techrepublic.com/rssfeeds/articles/']
        self.loaded_feed = self.rss.parse(self.load_feed_url[0])
        self.test_feed = self.loaded_feed.get_current()
        _list = []
        _feed_one = {
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
        }
        _feed_two = {
            'title': "Coronavirus: Supermarkets ask shoppers to be 'considerate' and stop panic buying",
            'title_detail': {
                'type': 'text/plain',
                'language': None,
                'base': 'http://feeds.bbci.co.uk/news/rss.xml',
                'value': "Coronavirus: Supermarkets ask shoppers to be 'considerate' and stop panic buying"
            },
            'summary': 'Some UK retailers have started rationing products such as pasta and hand gels to stop them selling out.',
            'summary_detail': {
                'type': 'text/html',
                'language': None,
                'base': 'http://feeds.bbci.co.uk/news/rss.xml',
                'value': 'Some UK retailers have started rationing products such as pasta and hand gels to stop them selling out.'
            },
            'links': [
                {
                    'rel': 'alternate',
                    'type': 'text/html',
                    'href': 'https://www.bbc.co.uk/news/business-51883440'
                }
            ],
            'link': 'https://www.bbc.co.uk/news/business-51883440',
            'id': 'https://www.bbc.co.uk/news/business-51883440',
            'guidislink': False,
            'published': 'Sun, 15 Mar 2020 00:00:35 GMT',
        }
        _list.append(_feed_one)
        _list.append(_feed_two)
        self._return_value_null = {'entries': _list, 'feed': {
            'title': 'BBC',
            'subtitle': 'BBC News - Home',
            'link': 'https://www.bbc.co.uk/news/'
        }}
        pass

    def test_next_url(self):
        self.ctr.list_urls = self.loaded_urls
        _url = self.ctr.next_url()
        assert _url == 'http://anotherfake.com'
        with self.assertRaises(Exception): self.ctr.next_url()

    def test_feed(self):
        _url = self.load_feed_url[0]
        _rss_model = RssModel().parse(_url)
        _newsreel = _rss_model.get_current()
        self.assertTrue(_newsreel, self.ctr.next_feed(_url))

    def test_main_fail(self):
        with patch.object(yaml, 'load', return_value={}) as mock_method:
            with mock.patch('builtins.open', self._mock_open):
                with self.assertRaises(Exception): self.ctr.main()
                assert self.ctr.list_urls is None

    def test_run(self):
        with patch.object(RssController, 'next_feed', return_value={}) as mock_method:
            self.ctr.list_urls = ['http://fake.com', 'http://fakeagain.com']
            self.ctr.run()
            assert self.ctr.url_index_pos == len(self.ctr.list_urls)
            self.ctr.list_urls = ['http://fake.com', 'http://fakeagain.com', 'http://superfake.com']
            self.ctr.run()
            assert self.ctr.url_index_pos == len(self.ctr.list_urls)

    def test_next_url_fail(self):
        self.ctr.list_urls = []
        with self.assertRaises(Exception): self.ctr.next_url()

    def test_reset_url_index(self):
        self.ctr.reset_url_index()
        assert self.ctr.url_index_pos == 0

    def test_next_index(self):
        self.ctr.next_index()
        assert self.ctr.url_index_pos == 1

    """This exception should be passed to the view, the view then should display the exception in a user friendly 
    manner. """

    def test_load_urls(self):
        with patch.object(yaml, 'load', return_value=self._return_value) as mock_method:
            with mock.patch('builtins.open', self._mock_open):
                _settings = SettingsModel()
                _settings.filename = 'dummy.yaml'
                _loaded_settings = _settings.load_settings().settings
                assert _loaded_settings['feeds'] == self._return_value['feeds']
                list_urls = self.ctr.load_urls()
                self.assertIs(type(list_urls), list)
                assert list_urls == self._return_value['feeds']

    def test_load_settings_no_file(self):
        with patch.object(yaml, 'load', return_value=self._return_value) as mock_method:
            with self.assertRaises(Exception):
                _settings = SettingsModel()
                _settings.filename = 'ghost_file.yaml'
                _settings.load_settings()

    def test_load_settings(self):
        with patch.object(yaml, 'load', return_value=self._return_value) as mock_method:
            with mock.patch('builtins.open', self._mock_open):
                _settings = SettingsModel()
                _settings.filename = 'dummy.yaml'
                _loaded_settings = _settings.load_settings().settings
                assert _loaded_settings['feeds'] == self._return_value['feeds']

    def test_save_settings(self):
        _settings = SettingsModel()
        _settings.filename = 'dummy_.yaml'
        _settings.save_settings(self._return_value)
        assert _settings.load_settings().settings['feeds'] == self._return_value['feeds']
        os.remove(_settings.filename)

    def test_save_settings_again(self):
        _settings = SettingsModel()
        _settings.filename = 'dummy_.yaml'
        _settings.settings = self._return_value
        _settings.save_settings()
        assert _settings.load_settings().settings['feeds'] == self._return_value['feeds']
        os.remove(_settings.filename)

    def test_parse(self):
        with patch.object(feedparser, 'parse', return_value=self._return_value_null) as mock_method:
            rss = self.rss.parse('http://fakeurl.com')
            assert rss.title == 'BBC'
            assert rss.subtitle == 'BBC News - Home'
            assert rss.link == 'https://www.bbc.co.uk/news/'
            assert len(rss.newsreel) > 0
            assert rss.newsreel[0]['title'] is not None
            assert rss.newsreel[1]['title'] is not None

    def test_get_current(self):
        with patch.object(feedparser, 'parse', return_value=self._return_value_null) as mock_method:
            self.rss.parse('http://fakeurl.com')
            value = self.rss.get_current()
            assert self.rss._newsreel_index_pos == -1
            assert len(value) > 0
            assert value['title'] == 'Coronavirus: UK deaths double in 24 hours'
            assert value[
                       'summary'] == 'Ten more people have died after testing positive for the virus, NHS England says.'
            assert value['link'] == 'https://www.bbc.co.uk/news/uk-51889957'

    def test_get_next(self):
        with patch.object(feedparser, 'parse', return_value=self._return_value_null) as mock_method:
            self.rss.parse('http://fakeurl.com')
            self.rss._newsreel_index_pos = 0
            value = self.rss.get_next()
            assert self.rss._newsreel_index_pos == 1
            assert len(value) > 0
            assert value['title'] == 'Coronavirus: Supermarkets ask shoppers to be \'considerate\' and stop panic buying'
            assert value['summary'] == 'Some UK retailers have started rationing products such as pasta and hand gels to stop them selling out.'
            assert value['link'] == 'https://www.bbc.co.uk/news/business-51883440'

    def test_parse_fail(self):
        with patch.object(feedparser, 'parse', return_value={}) as mock_method:
            with self.assertRaises(Exception): self.rss.parse('http://givemeanexception.com')

    def test_get_current_no_news_loaded_fail(self):
        self.rss = RssModel()
        with patch.object(feedparser, 'parse', return_value={}) as mock_method:
            with self.assertRaises(Exception): self.rss.get_current()

    def test_get_next_no_news_loaded_fail(self):
        self.rss = RssModel()
        with patch.object(feedparser, 'parse', return_value={}) as mock_method:
            with self.assertRaises(Exception): self.rss.get_next()

    def test_get_current_no_newsreel_fail(self):
        with patch.object(feedparser, 'parse', return_value=self._return_value_null) as mock_method:
            self.rss.parse('http://fakeurl.com')
            self.rss.newsreel = []
            with self.assertRaises(Exception): self.rss.get_current()

    def test_get_next_out_of_bounds_fail(self):
        self.rss = RssModel()
        with patch.object(feedparser, 'parse', return_value=self._return_value_null) as mock_method:
            self.rss.parse('http://fakeurl.com')
            self.rss._newsreel_index_pos = 42
            with self.assertRaises(Exception): self.rss.get_next()

    def test_parse_fail_not_string(self):
        with patch.object(feedparser, 'parse', return_value={}) as mock_method:
            with self.assertRaises(Exception): self.rss.parse({'http://givemeanexception.com'})

    def test_start(self):
        """Checks functionality of .mainloop()"""
        with patch('RSS.view.userinterface.tk.Tk') as mock_window:
            root = tk.Tk()
            app = ui.RSSticker(master=root)
            app.start()
            mock_window.assert_has_calls(mock_window.mainloop())

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
