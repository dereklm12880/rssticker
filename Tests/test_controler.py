# https://ongspxm.github.io/blog/2016/11/assertraises-testing-for-errors-in-unittest/
import unittest
from unittest.mock import patch, Mock
from RSS.controller.controler import RssController


class TestRssModel(unittest.TestCase):

    def setUp(self):
        self.rss = Mock()
        self.view = Mock()
        self.ctr = RssController()
        self.rss_url_list = None
        self.loaded_urls = ['http://fake.com', 'http://anotherfake.com']
        pass

    def test_next_url(self):
        ctr.urls = self.loaded_urls
        _url = ctr.next_url()
        assert _url == 'http://fake.com'
        _url = ctr.next_url()
        assert _url == 'http://anotherfake.com'
        with self.assertRaises(Exception): ctr.next_url()

    def test_next_url_fail(self):
        ctr.urls = []
        with self.assertRaises(Exception): ctr.next_url()

    """This exception should be passed to the view, the view then should display the exception in a user friendly 
    manner. """
    def test_load_file_fail(self):
        ctr.filename='NotRealFile.txt'
        with self.assertRaises(Exception): ctr.load_file()




