import os
import unittest
from unittest import mock
import yaml
from mock import patch
from RSS.model.style import style_default



class test_style(unittest.Testcase):

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

    def test_check_style(self):
        with patch.object(style_default().check_style(),'settings_list', test_result=input_value) as mock_method:
        # with patch('RSS.model.style.style_default')
        #     assert self.test_result == self.return_value
            self.assertEqual(self.test)

    def test_check_dump(self):
        _settings = style_default()
        _settings.filename = 'dummy_.yaml'
        _settings.check_dump(self._return_value)
        assert _settings.check_dump().input_value == self.return_value
        os.remove(_settings.filename)

        # result = style_default.check_style(self.input_value)
        # self.assertEqual(result, self.return_value)



if __name__ == "__main__":
    unittest.main()
    # test_style().test_check_style()
    # test_style().test_check_dump()
