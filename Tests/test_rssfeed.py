# https://ongspxm.github.io/blog/2016/11/assertraises-testing-for-errors-in-unittest/
import unittest
from mock import patch
from RSS.model.rssfeed import RssModel
import feedparser


class TestRssModel(unittest.TestCase):
    _return_value = {}

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
        self._return_value = {'entries': _list, 'feed': {
            'title': 'BBC',
            'subtitle': 'BBC News - Home',
            'link': 'https://www.bbc.co.uk/news/'
        }}
        pass

    def test_parse(self):
        with patch.object(feedparser, 'parse', return_value=self._return_value) as mock_method:
            rss = self.rss.parse('http://fakeurl.com')
            assert rss.title == 'BBC'
            assert rss.subtitle == 'BBC News - Home'
            assert rss.link == 'https://www.bbc.co.uk/news/'
            assert len(rss.newsreel) > 0
            assert rss.newsreel[0]['title'] is not None
            assert rss.newsreel[1]['title'] is not None

    def test_get_current(self):
        with patch.object(feedparser, 'parse', return_value=self._return_value) as mock_method:
            self.rss.parse('http://fakeurl.com')
            value = self.rss.get_current()
            assert self.rss._newsreel_index_pos == 0
            assert len(value) > 0
            assert value['title'] == 'Coronavirus: UK deaths double in 24 hours'
            assert value[
                       'summary'] == 'Ten more people have died after testing positive for the virus, NHS England says.'
            assert value['link'] == 'https://www.bbc.co.uk/news/uk-51889957'

    def test_get_next(self):
        with patch.object(feedparser, 'parse', return_value=self._return_value) as mock_method:
            self.rss.parse('http://fakeurl.com')
            value = self.rss.get_next()
            assert self.rss._newsreel_index_pos == 1
            assert len(value) > 0
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
        with patch.object(feedparser, 'parse', return_value=self._return_value) as mock_method:
            self.rss.parse('http://fakeurl.com')
            self.rss.newsreel = []
            with self.assertRaises(Exception): self.rss.get_current()

    def test_get_next_out_of_bounds_fail(self):
        with patch.object(feedparser, 'parse', return_value=self._return_value) as mock_method:
            self.rss.parse('http://fakeurl.com')
            self.rss._newsreel_index_pos = 42
            with self.assertRaises(Exception): self.rss.get_current()

    def test_parse_fail_not_string(self):
        with patch.object(feedparser, 'parse', return_value={}) as mock_method:
            with self.assertRaises(Exception): self.rss.parse({'http://givemeanexception.com'})
