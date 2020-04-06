# https://ongspxm.github.io/blog/2016/11/assertraises-testing-for-errors-in-unittest/
import unittest
from mock import MagicMock

from RSS.controller.controler import RssController
from RSS.model.rssfeed import RssModel


class TestRssModel(unittest.TestCase):

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
        assert _url == 'http://fake.com'
        _url = self.ctr.next_url()
        assert _url == 'http://anotherfake.com'
        with self.assertRaises(Exception): self.ctr.next_url()

    def test_feed(self):
        self.ctr.filename = '../RSS/controller/list_urls.csv'
        self.ctr.list_urls = self.load_feed_url
        _url = self.load_feed_url
        _rss_model = self.ctr.rss_model.parse(_url[0])
        _newsreel = _rss_model.get_current()
        self.assertTrue(_newsreel, self.ctr.main())

    def test_next_url_fail(self):
        self.ctr.list_urls = []
        with self.assertRaises(Exception): self.ctr.next_url()

    """This exception should be passed to the view, the view then should display the exception in a user friendly 
    manner. """

    def test_load_file_fail(self):
        self.ctr.filename = 'NotRealFile.txt'
        with self.assertRaises(Exception): self.ctr.load_urls()
        self.ctr.filename = '../RSS/controller/testing_urls.csv'
        with self.assertRaises(Exception): self.ctr.main()

    def test_load_urls(self):
        self.ctr.filename = '../RSS/controller/testing_urls.csv'
        list_urls = self.ctr.load_urls()
        self.assertIs(type(list_urls), list)
