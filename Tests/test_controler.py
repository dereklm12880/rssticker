# https://ongspxm.github.io/blog/2016/11/assertraises-testing-for-errors-in-unittest/

import unittest
from unittest.mock import patch
import sys
sys.path.append("../")
from RSS.model.rssfeed import RssModel
import feedparser

class TestRssModel(unittest.TestCase):
    def setUp(self):
          self.rss=Mock()
        self.view=Mock()
        self.ctr=RssController()
        self.rss_url_list=None
        self.loaded_urls=['http://fake.com', 'http://anotherfake.com']
        pass

    def test_next_url(self):
        self.ctr.list_urls = self.loaded_urls
        _url = self.ctr.next_url()
        assert _url == 'http://fake.com'
        _url = self.ctr.next_url()
        assert _url == 'http://anotherfake.com'
        with self.assertRaises(Exception): self.ctr.next_url()

    # def test_feed_cycle(self):
    #     self.ctr.list_urls = self.load_feed_url
    #     _url = self.load_feed_url
    #     _rss_model = self.ctr.rss_model.parse(_url[0])
    #     _newsreel = _rss_model.get_current()
    #     assert _newsreel == self.ctr.main()

    def test_next_url_fail(self):
        self.ctr.urls = []
        with self.assertRaises(Exception): self.ctr.next_url()

    """This exception should be passed to the view, the view then should display the exception in a user friendly 
    manner. """

    def test_load_file_fail(self):
        self.ctr.filename = 'NotRealFile.txt'
        with self.assertRaises(Exception): self.ctr.load_urls()
