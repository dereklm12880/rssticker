# https://ongspxm.github.io/blog/2016/11/assertraises-testing-for-errors-in-unittest/
import unittest
from unittest import mock
from unittest.mock import patch, Mock
<<<<<<< HEAD
from RSS.controller.controler import RssController
from RSS.model.rssfeed import RssModel
=======
from RSS.controller.rssfeed import RssController
from RSS.model.rssfeed import RssModel
from RSS.model.settings import SettingsModel
>>>>>>> origin/feature/alanis


class TestRssModel(unittest.TestCase):
    _return_value = {"feeds": ["http://fakefeed.com", "http://anotherfakefeed.com"]}
    _mock_open = mock.mock_open(read_data='')
    _dummy_yaml_file_settings_no_feeds = {'color': ['#000']}
    _dummy_yaml_file_settings_with_feeds = {'feeds': ['http://preexisting.com']}
    _dummy_yaml_file_settings_with_feeds_and_others = {'color': ['#000'], 'feeds': ['http://preexisting.com']}

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

<<<<<<< HEAD
    def test_next_url(self):
        self.ctr.list_urls = self.loaded_urls
        _url = self.ctr.next_url()
        assert _url == 'http://fake.com'
        _url = self.ctr.next_url()
        assert _url == 'http://anotherfake.com'
        with self.assertRaises(Exception): self.ctr.next_url()

    def test_feed(self):
        _url = self.load_feed_url
        _rss_model = self.ctr.rss_model.parse(_url[0])
        _newsreel = _rss_model.get_current()
        self.assertTrue(_newsreel, self.ctr.next_feed(_url))

    def test_next_url_fail(self):
        self.ctr.list_urls = []
        with self.assertRaises(Exception): self.ctr.next_url()

    """This exception should be passed to the view, the view then should display the exception in a user friendly 
    manner. """

    def test_load_file_fail(self):
        self.ctr.filename = 'NotRealFile.txt'
        with self.assertRaises(Exception): self.ctr.load_urls()
        self.ctr.filename = '../testing_urls.csv'
        with self.assertRaises(Exception): self.ctr.main()

    def test_load_urls(self):
         self.ctr.filename = '../testing_urls.csv'
         list_urls = self.ctr.load_urls()
         self.assertIs(type(list_urls), list)
=======
    def test_next_feed(self):
        _next = self.ctr.next_feed()
        assert isinstance(_next, RssModel)

    def test_next_feed_fail_invalid_url(self):
        with self.assertRaises(Exception): _next = self.ctr.next_feed('abc')

    def test_next_feed_fail_no_feeds(self):
        self.ctr.settings_model.settings = {}
        with self.assertRaises(Exception): self.ctr.next_feed(self.load_feed_url)

    def _dump(self, settings):
        self.ctr.settings_model.settings = settings

    def test_save_settings_no_settings(self):
        with patch.object(SettingsModel, 'load_settings', return_value={}) as mock_method:
            with patch.object(SettingsModel, 'save_settings', new=self._dump) as mock_method:
                self.ctr.settings_model.settings = self.ctr.settings_model.load_settings()
                settings = {'feeds': ['https://fake.com']}
                self.ctr.save_settings(settings)
                assert self.ctr.settings_model.settings == settings

    def test_save_settings_with_settings_no_feeds(self):
        with patch.object(SettingsModel, 'load_settings',
                          return_value=self._dummy_yaml_file_settings_no_feeds) as mock_method:
            with patch.object(SettingsModel, 'save_settings', new=self._dump) as mock_method:
                self.ctr.settings_model.settings = self.ctr.settings_model.load_settings()
                settings = {'feeds': ['https://fake.com']}
                self.ctr.save_settings(settings)
                settings.update(self._dummy_yaml_file_settings_no_feeds)
                assert self.ctr.settings_model.settings == settings

    def test_save_settings_with_settings_with_feeds(self):
        with patch.object(SettingsModel, 'load_settings',
                          return_value=self._dummy_yaml_file_settings_with_feeds) as mock_method:
            with patch.object(SettingsModel, 'save_settings', new=self._dump) as mock_method:
                self.ctr.settings_model.settings = self.ctr.settings_model.load_settings()
                settings = {'feeds': ['https://fake.com']}
                self.ctr.save_settings(settings)
                settings.update(self._dummy_yaml_file_settings_with_feeds)
                assert self.ctr.settings_model.settings == {'feeds': ['https://fake.com']}

    def test_save_settings_with_settings_with_feeds_with_other(self):
        self.ctr.settings_model.filename = 'dummy.yaml'
        with patch.object(SettingsModel, 'load_settings',
                          return_value=self._dummy_yaml_file_settings_with_feeds_and_others) as mock_method:
            with patch.object(SettingsModel, 'save_settings', new=self._dump) as mock_method:
                self.ctr.settings_model.settings = self.ctr.settings_model.load_settings()
                settings = {'feeds': ['https://fake.com']}
                self.ctr.save_settings(settings)
                settings.update(self._dummy_yaml_file_settings_with_feeds_and_others)
                assert self.ctr.settings_model.settings == {'color': ['#000'],
                                                            'feeds': ['https://fake.com']}

    def test_save_settings_with_settings_feeds(self):
        self.ctr.settings_model.filename = 'dummy.yaml'
        with patch.object(SettingsModel, 'load_settings',
                          return_value=self._dummy_yaml_file_settings_with_feeds_and_others) as mock_method:
            with patch.object(SettingsModel, 'save_settings', new=self._dump) as mock_method:
                self.ctr.settings_model.settings = self.ctr.settings_model.load_settings()
                settings = {'feeds': ['https://fake.com']}
                self.ctr.save_settings(settings)
                assert self.ctr.settings_model.settings == {'color': ['#000'],
                                                            'feeds': ['https://fake.com']}
>>>>>>> origin/feature/alanis
