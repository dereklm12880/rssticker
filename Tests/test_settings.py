import os
import unittest
from unittest import mock
import yaml
from mock import patch
from RSS.model.settings import SettingsModel
import builtins


class TestRssSettings(unittest.TestCase):

    """Test class for RSS.model.settings.SettingsModel."""

    _return_value = {"feeds": ["http://fakefeed.com", "http://anotherfakefeed.com"]}
    _mock_open = mock.mock_open(read_data='')

    def test_load_settings_no_file(self):
        """ Unit test for RSSmodel.model.settings.SettingsModel.load_settings.
        Tests to make sure that the .yaml file exists.
        """
        with patch.object(yaml, 'load', return_value=self._return_value) as mock_method:
            with self.assertRaises(Exception):
                _settings = SettingsModel()
                _settings.filename = 'ghost_file.yaml'
                _settings.load_settings()

    def test_load_settings(self):
        """ Unit test for RSSmodel.model.settings.SettingsModel.next_url.
        Tests to check feeds in yaml file that can be loaded.
        """
        with patch.object(yaml, 'load', return_value=self._return_value) as mock_method:
            with mock.patch('builtins.open', self._mock_open):
                _settings = SettingsModel()
                _settings.filename = 'dummy.yaml'
                _loaded_settings = _settings.load_settings().settings
                assert _loaded_settings['feeds'] == self._return_value['feeds']

    def test_save_settings(self):
        """ Unit test for RSSmodel.model.settings.SettingsModel.save_settings.
        Tests to check a dictionary of configurable values to be converted into the yaml file. 
        """
        _settings = SettingsModel()
        _settings.filename = 'dummy_.yaml'
        _settings.save_settings(self._return_value)
        assert _settings.load_settings().settings['feeds'] == self._return_value['feeds']
        os.remove(_settings.filename)

    def test_save_settings_again(self):
        """ Unit test for RSSmodel.model.settings.SettingsModel.save_settings.
        Tests to check a dictionary of configurable values to be converted into the yaml file. 
        """
        _settings = SettingsModel()
        _settings.filename = 'dummy_.yaml'
        _settings.settings = self._return_value
        _settings.save_settings()
        assert _settings.load_settings().settings['feeds'] == self._return_value['feeds']
        os.remove(_settings.filename)

    def test_save_settings_fail_set_via_settings_class_member(self):
        """ Unit test for RSSmodel.model.settings.SettingsModel.save_settings.
        Tests to check the function is throwing an exception because of the settings class.
        """
        _settings = SettingsModel()
        _settings.filename = 'dummy_.yaml'
        _settings.settings = 'Bob dole was here'
        with self.assertRaises(Exception):
            _settings.save_settings()

    def test_save_settings_fail_set_via_argument(self):
        """ Unit test for RSSmodel.model.settings.SettingsModel.save_settings.
        Tests to check the function is throwing an exception because the argument is invalid.
        """
        _settings = SettingsModel()
        _settings.filename = 'dummy_.yaml'
        with self.assertRaises(Exception):
            _settings.save_settings(12345)

    def test_next_url(self):
        """ Unit test for RSSmodel.model.settings.SettingsModel.next_url.
        Tests to assert that are are valid feeds in the yaml file.
        """
        with patch.object(yaml, 'load', return_value=self._return_value) as mock_method:
            _settings = SettingsModel()
            _settings.filename = 'dummy.yaml'
            _settings.load_settings()
            _url = _settings.next_url()
            assert _url == 'http://fakefeed.com'
            _url = _settings.next_url()
            assert _url == 'http://anotherfakefeed.com'
            _url = _settings.next_url()
            assert _url == 'http://fakefeed.com'

    def test_next_url_with_exception(self):
        """ Unit test for RSSmodel.model.settings.SettingsModel.next_url.
        Tests to check that the function is throwing an exception when the return value is empty.
        """
        with patch.object(yaml, 'load', return_value={}) as mock_method:
            _settings = SettingsModel()
            _settings.filename = 'dummy.yaml'
            _settings.load_settings()
            with self.assertRaises(Exception):
                _url = _settings.next_url()
