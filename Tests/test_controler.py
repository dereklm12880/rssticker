# https://ongspxm.github.io/blog/2016/11/assertraises-testing-for-errors-in-unittest/
import unittest
from unittest import mock
from unittest.mock import patch, Mock

import yaml

from RSS.controller.rssfeed import RssController
from RSS.model.rssfeed import RssModel
from RSS.model.settings import SettingsModel


class TestRssModel(unittest.TestCase):
    _return_value = {"feeds": ["http://fakefeed.com", "http://anotherfakefeed.com"]}
    _mock_open = mock.mock_open(read_data='')

    def setUp(self):
        self.rss = RssModel()
        self.view = Mock()
        self.ctr = RssController()
        self.rss_url_list = None
        self.loaded_urls = ['http://fake.com', 'http://anotherfake.com']
        self.load_feed_url = ['https://www.techrepublic.com/rssfeeds/articles/']
        self.loaded_feed = self.rss.parse(self.load_feed_url[0])
        self.test_feed = self.loaded_feed.get_current()
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
