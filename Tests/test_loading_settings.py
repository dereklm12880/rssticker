import os
import unittest
from unittest import mock
import yaml
from mock import patch
from RSS.model.settings import SettingsModel
import builtins


class TestRssModel(unittest.TestCase):
    _return_value = {"feeds": ["http://fakefeed.com", "http://anotherfakefeed.com"]}
    _mock_open = mock.mock_open(read_data='')

    def test_load_settings_no_file(self):
        with patch.object(yaml, 'load', return_value=self._return_value) as mock_method:
            with self.assertRaises(Exception):
                _settings = SettingsModel()
                _settings.filename = 'ghost_file.yaml'
                _settings.load_settings()

    def test_load_settings(self):
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