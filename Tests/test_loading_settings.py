import unittest
from mock import patch
from RSS.model.settings import SettingsModel
import feedparser


class TestRssModel(unittest.TestCase):
    settings=None
    def setUp(self):
        self.settings = SettingsModel()

   def test_load_settings(self):

       pass

   def test_get_file(self):
       pass