import unittest
from unittest.mock import patch
from Model.rssticker import RssModel


class TestRssTicker(unittest.TestCase):
    def setUp(self):
        self.rss = RssModel()
        pass

    def test_get_rss_feeds(self):
        with patch.object(RssModel, 'get_rss_feeds', return_value={'feed', 'entries'}) as mock_method:
            values = self.rss.get_rss_feeds()
            assert 'feed' in values
            assert 'entries' in values
