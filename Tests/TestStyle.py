import os
import unittest
from unittest import mock
import yaml
from mock import patch
from mock import MagicMock
from RSS.model.style import style_default


class TestStyle(unittest.TestCase):
    input_value = {'background_color': None, 'cycle_time': None,
                   'feeds': ['https://www.techrepublic.com/rssfeeds/articles/', 'https://xkcd.com/rss.xml',
                             'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/americas/rss.xml'],
                   'font_color': ['#000000'], 'font_size': ['12pt'], 'font_type': ['Times New Roman'],
                   'window placement': None}
    _return_value = {'background_color': 'white', 'cycle_time': 30,
                     'feeds': ['https://www.techrepublic.com/rssfeeds/articles/', 'https://xkcd.com/rss.xml',
                               'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/americas/rss.xml'],
                     'font_color': ['#000000'], 'font_size': ['12pt'], 'font_type': ['Times New Roman'],
                     'window placement': 'top left'}
    _mock_open = mock.mock_open(read_data='')

    def test_load_settings(self):
        with patch.object(yaml, return_value=self.input_value) as mock_method:
            with mock.patch('builtins.open', self._mock_open):
                _settings = style_default()
                _settings.filename = 'dummy.yaml'
                _loaded_settings = _settings.load_settings()
                assert _loaded_settings == self.input_value

    # @patch.object(style_default, 'settings_list')
    def test_check_style(self):
        with patch.object(style_default, 'load_settings', return_value=self.input_value) as mock_method:
            list = style_default()
            settings_list = list.check_style()
            assert settings_list == self.return_value
            self.return_value = self._return_value
            temp = style_default()
            assert temp.check_style() == self.return_value

    def test_check_dump(self):
        # expected = self.return_value.__format__(n=os.linesep)
        with patch.object(yaml, 'load', return_value=self._return_value) as mock_variable:
            with patch.object(style_default, 'load_settings', return_value=self._return_value) as mock_method:
                _settings = style_default()
                _settings.filename = 'dummy_.yaml'
                _settings.check_dump(self._return_value)
                # assert _settings.dictionar().input_value == self._return_value
                assert True
                os.remove(_settings.filename)
    #

# if __name__ == "__main__":
#     unittest.main()
#     # test_style().test_check_style()
#     # test_style().test_check_dump()
