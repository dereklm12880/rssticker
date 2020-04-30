import os
import unittest
from unittest import mock
import yaml
from mock import patch
from RSS.model.style import style_default



class TestStyle(unittest.Testcase):

    input_value = {'background_color': None, 'cycle_time': None,
                   'feeds': ['https://www.techrepublic.com/rssfeeds/articles/', 'https://xkcd.com/rss.xml',
                             'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/americas/rss.xml'],
                   'font_color': ['#000000'], 'font_size': ['12pt'], 'font_type': ['Times New Roman'],
                   'window placement': None}
    return_value = {'background_color': 'white', 'cycle_time': 30,
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

    def test_check_style(self):
        with patch.object(style_default.load_settings(), 'settings_list', return_value=self.input_value):
            self.assertEquals(self.return_value,style_default.check_style())


    def test_check_dump(self):
        _settings = style_default()
        _settings.filename = 'dummy_.yaml'
        _settings.check_dump(self._return_value)
        assert _settings.check_dump().input_value == self.return_value
        os.remove(_settings.filename)

        # result = style_default.check_style(self.input_value)
        # self.assertEqual(result, self.return_value)



# if __name__ == "__main__":
#     unittest.main()
#     # test_style().test_check_style()
#     # test_style().test_check_dump()
