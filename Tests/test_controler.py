# https://ongspxm.github.io/blog/2016/11/assertraises-testing-for-errors-in-unittest/
import unittest
from unittest import mock
from unittest.mock import patch, Mock
from RSS.controller.rssfeed import RssController
from RSS.model.rssfeed import RssModel
from RSS.model.settings import SettingsModel


class TestRssModel(unittest.TestCase):

    """Test class for RSS.controller.rssfeed.RssController."""

    _return_value = {"feeds": ["http://fakefeed.com", "http://anotherfakefeed.com"]}
    _mock_open = mock.mock_open(read_data='')
    _dummy_yaml_file_settings_no_feeds = {'color': ['#000']}
    _dummy_yaml_file_settings_with_feeds = {'feeds': ['http://preexisting.com']}
    _dummy_yaml_file_settings_with_feeds_and_others = {'color': ['#000'], 'feeds': ['http://preexisting.com']}

    def setUp(self):

        """Function that sets up the unittest for the RssController"""

        self.rss = RssModel()
        self.view = Mock()
        self.ctr = RssController()
        self.rss_url_list = None
        self.loaded_urls = ['http://fake.com', 'http://anotherfake.com']
        self.load_feed_url = ['https://www.techrepublic.com/rssfeeds/articles/']
        self.loaded_feed = self.rss.parse(self.load_feed_url[0])
        self.test_feed = self.loaded_feed.get_current()
        pass

    def test_next_feed(self):
        """ Unit test for RSS.controller.rssfeed.RssController.next_feed.
        Test to check that the function returns the feeds parsed in the model.
        """
        _next = self.ctr.next_feed()
        assert isinstance(_next, RssModel)

    def test_next_feed_fail_invalid_url(self):
        """ Unit test for RSS.controller.rssfeed.RssController.next_feed.
        Test to check the function is throwing an exception because of an invalid url.
        """
        with patch.object(SettingsModel, 'next_url', return_value="abc"):
            _ctr = RssController()
            with self.assertRaises(Exception):
                _ctr.next_feed()

    def test_next_feed_fail_no_feeds(self):
        """ Unit test for RSS.controller.rssfeed.RssController.next_feed.
        Test to check the function is throwing an exception because there are no feeds.
        """
        self.ctr.settings_model.settings = {}
        with self.assertRaises(Exception): self.ctr.next_feed(self.load_feed_url)

    def _dump(self, settings):
        self.ctr.settings_model.settings = settings

    def test_save_settings_no_settings(self):
        """ Unit test for RSS.controller.rssfeed.RssController.save_settings.
        Test to check the save settings function is saving settings into the yaml file with no settings.
        """
        with patch.object(SettingsModel, 'load_settings', return_value={}) as mock_method:
            with patch.object(SettingsModel, 'save_settings', new=self._dump) as mock_method:
                self.ctr.settings_model.settings = self.ctr.settings_model.load_settings()
                settings = {'feeds': ['https://fake.com']}
                self.ctr.save_settings(settings)
                assert self.ctr.settings_model.settings == settings

    def test_save_settings_with_settings_no_feeds(self):
        """ Unit test for RSS.controller.rssfeed.RssController.save_settings.
        Test to check the save settings function is saving settings into the yaml file with no feeds.
        """
        with patch.object(SettingsModel, 'load_settings',
                          return_value=self._dummy_yaml_file_settings_no_feeds) as mock_method:
            with patch.object(SettingsModel, 'save_settings', new=self._dump) as mock_method:
                self.ctr.settings_model.settings = self.ctr.settings_model.load_settings()
                settings = {'feeds': ['https://fake.com']}
                self.ctr.save_settings(settings)
                settings.update(self._dummy_yaml_file_settings_no_feeds)
                assert self.ctr.settings_model.settings == settings

    def test_save_settings_with_settings_with_feeds(self):
        """ Unit test for RSS.controller.rssfeed.RssController.save_settings.
        Test to check the save settings function is saving settings into the yaml file with feeds.
        """
        with patch.object(SettingsModel, 'load_settings',
                          return_value=self._dummy_yaml_file_settings_with_feeds) as mock_method:
            with patch.object(SettingsModel, 'save_settings', new=self._dump) as mock_method:
                self.ctr.settings_model.settings = self.ctr.settings_model.load_settings()
                settings = {'feeds': ['https://fake.com']}
                self.ctr.save_settings(settings)
                settings.update(self._dummy_yaml_file_settings_with_feeds)
                assert self.ctr.settings_model.settings == {'feeds': ['https://fake.com']}

    def test_save_settings_with_settings_with_feeds_with_other(self):
        """ Unit test for RSS.controller.rssfeed.RssController.save_settings.
        Another test to check the save settings function is saving settings into the yaml file with feeds.
        """
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
        """ Unit test for RSS.controller.rssfeed.RssController.save_settings.
        Another test to check the save settings function is saving settings into the yaml file with feeds.
        """
        self.ctr.settings_model.filename = 'dummy.yaml'
        with patch.object(SettingsModel, 'load_settings',
                          return_value=self._dummy_yaml_file_settings_with_feeds_and_others) as mock_method:
            with patch.object(SettingsModel, 'save_settings', new=self._dump) as mock_method:
                self.ctr.settings_model.settings = self.ctr.settings_model.load_settings()
                settings = {'feeds': ['https://fake.com']}
                self.ctr.save_settings(settings)
                assert self.ctr.settings_model.settings == {'color': ['#000'],
                                                            'feeds': ['https://fake.com']}