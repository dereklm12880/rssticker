from unittest.mock import patch, Mock
from RSS.controller.rssfeed import RssController
import os
from unittest import mock
import yaml
from RSS.model.settings import SettingsModel
import unittest
from mock import patch
from RSS.model.rssfeed import RssModel
import feedparser

class TestAll(unittest.TestCase):
    _return_value = {"feeds": ["http://fakefeed.com", "http://anotherfakefeed.com"]}
    _mock_open = mock.mock_open(read_data='')
    _dummy_yaml_file_settings_no_feeds = {'color': ['#000']}
    _dummy_yaml_file_settings_with_feeds = {'feeds': ['http://preexisting.com']}
    _dummy_yaml_file_settings_with_feeds_and_others = {'color': ['#000'], 'feeds': ['http://preexisting.com']}
    _return_value = {"feeds": ["http://fakefeed.com", "http://anotherfakefeed.com"]}
    _mock_open = mock.mock_open(read_data='')
    _return_value_null = {}
    ctr = None
    rss = RssModel()
    view = Mock()
    ctr = RssController()
    rss_url_list = None
    loaded_urls = ['http://fake.com', 'http://anotherfake.com']
    load_feed_url = ['https://www.techrepublic.com/rssfeeds/articles/']
    loaded_feed = rss.parse(load_feed_url[0])
    test_feed = loaded_feed.get_current()
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
    _return_value_null = {'entries': _list, 'feed': {
        'title': 'BBC',
        'subtitle': 'BBC News - Home',
        'link': 'https://www.bbc.co.uk/news/'
    }}

    def test_next_feed(self):
        self.ctr = RssController()
        _next = self.ctr.next_feed()
        assert isinstance(_next, RssModel)

    def test_next_feed_fail_invalid_url(self):
        with self.assertRaises(Exception): _next = self.ctr.next_feed('abc')

    def test_next_feed_fail_no_feeds(self):
        self.ctr = RssController()
        self.ctr.settings_model.settings = {}
        with self.assertRaises(Exception): self.ctr.next_feed(self.load_feed_url)

    def _dump(self, settings):
        self.ctr.settings_model.settings = settings

    def test_save_settings_no_settings(self):
        self.ctr = RssController()
        with patch.object(SettingsModel, 'load_settings', return_value={}) as mock_method:
            with patch.object(SettingsModel, 'save_settings', new=self._dump) as mock_method:
                self.ctr.settings_model.settings = self.ctr.settings_model.load_settings()
                settings = {'feeds': ['https://fake.com']}
                self.ctr.save_settings(settings)
                assert self.ctr.settings_model.settings == settings

    def test_save_settings_with_settings_no_feeds(self):
        self.ctr = RssController()

        with patch.object(SettingsModel, 'load_settings',
                          return_value=self._dummy_yaml_file_settings_no_feeds) as mock_method:
            with patch.object(SettingsModel, 'save_settings', new=self._dump) as mock_method:
                self.ctr.settings_model.settings = self.ctr.settings_model.load_settings()
                settings = {'feeds': ['https://fake.com']}
                self.ctr.save_settings(settings)
                settings.update(self._dummy_yaml_file_settings_no_feeds)
                assert self.ctr.settings_model.settings == settings

    def test_save_settings_with_settings_with_feeds(self):
        self.ctr = RssController()

        with patch.object(SettingsModel, 'load_settings',
                          return_value=self._dummy_yaml_file_settings_with_feeds) as mock_method:
            with patch.object(SettingsModel, 'save_settings', new=self._dump) as mock_method:
                self.ctr.settings_model.settings = self.ctr.settings_model.load_settings()
                settings = {'feeds': ['https://fake.com']}
                self.ctr.save_settings(settings)
                settings.update(self._dummy_yaml_file_settings_with_feeds)
                assert self.ctr.settings_model.settings == {'feeds': ['https://fake.com']}

    def test_save_settings_with_settings_with_feeds_with_other(self):
        self.ctr = RssController()

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
        self.ctr = RssController()
        self.ctr.settings_model.filename = 'dummy.yaml'
        with patch.object(SettingsModel, 'load_settings',
                          return_value=self._dummy_yaml_file_settings_with_feeds_and_others) as mock_method:
            with patch.object(SettingsModel, 'save_settings', new=self._dump) as mock_method:
                self.ctr.settings_model.settings = self.ctr.settings_model.load_settings()
                settings = {'feeds': ['https://fake.com']}
                self.ctr.save_settings(settings)
                assert self.ctr.settings_model.settings == {'color': ['#000'],
                                                            'feeds': ['https://fake.com']}
    def test_load_settings_no_file(self):
        self.ctr = RssController()
        with patch.object(yaml, 'load', return_value=self._return_value) as mock_method:
            with self.assertRaises(Exception):
                _settings = SettingsModel()
                _settings.filename = 'ghost_file.yaml'
                _settings.load_settings()

    def test_load_settings(self):
        self.ctr = RssController()
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

    def setUp(self):
        self.rss = RssModel()
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
            assert 'title' in value
            assert value['title'] == 'Coronavirus: UK deaths double in 24 hours'
            assert value[
                       'summary'] == 'Ten more people have died after testing positive for the virus, NHS England says.'
            assert value['link'] == 'https://www.bbc.co.uk/news/uk-51889957'

    def test_get_next(self):
        with patch.object(feedparser, 'parse', return_value=self._return_value_null) as mock_method:
            self.rss.parse('http://fakeurl.com')
            value = self.rss.get_next()
            assert self.rss._newsreel_index_pos == 0
            assert len(value) > 0
            assert value['title'] == 'Coronavirus: UK deaths double in 24 hours'
            assert value[
                       'summary'] == 'Ten more people have died after testing positive for the virus, NHS England says.'
            assert value['link'] == 'https://www.bbc.co.uk/news/uk-51889957'
            value = self.rss.get_next()
            assert value[
                       'title'] == 'Coronavirus: Supermarkets ask shoppers to be \'considerate\' and stop panic buying'
            assert value[
                       'summary'] == 'Some UK retailers have started rationing products such as pasta and hand gels to stop them selling out.'
            assert value['link'] == 'https://www.bbc.co.uk/news/business-51883440'

    def test_parse_fail(self):
        with patch.object(feedparser, 'parse', return_value={}) as mock_method:
            with self.assertRaises(Exception): self.rss.parse('http://givemeanexception.com')

    def test_get_current_no_news_loaded_fail(self):
        with patch.object(feedparser, 'parse', return_value={}) as mock_method:
            with self.assertRaises(Exception): self.rss.get_current()

    def test_get_next_no_news_loaded_fail(self):
        with patch.object(feedparser, 'parse', return_value={}) as mock_method:
            with self.assertRaises(Exception): self.rss.get_next()

    def test_get_current_no_newsreel_fail(self):
        with patch.object(feedparser, 'parse', return_value=self._return_value_null) as mock_method:
            self.rss.parse('http://fakeurl.com')
            self.rss.newsreel = []
            with self.assertRaises(Exception): self.rss.get_current()

    def test_get_next_out_of_bounds_fail(self):
        with patch.object(feedparser, 'parse', return_value=self._return_value_null) as mock_method:
            self.rss.parse('http://fakeurl.com')
            self.rss._newsreel_index_pos = 42
            with self.assertRaises(Exception): self.rss.get_current()

    def test_parse_fail_not_string(self):
        with patch.object(feedparser, 'parse', return_value={}) as mock_method:
            with self.assertRaises(Exception): self.rss.parse({'http://givemeanexception.com'})

