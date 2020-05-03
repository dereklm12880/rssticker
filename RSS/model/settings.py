from pathlib import Path
import yaml
from os import path


class SettingsModel:

    """ Class model.settings.SettingsModel.
    This class ensures the yaml file is loaded so that the feeds
    can be collected.
    """


    filename = str(Path(__file__).parents[2]) + '/settings.yaml'
    settings = {}
    _index = 0

    def load_settings(self):

        """ Function model.settings.SettingsModel.load_settings.
        This function ensures that the path to the configuration file exists
        and is correct. If not, it throws an exception, otherwise loading it.
        """

        if not path.exists(self.filename):
            raise Exception('No file exists {}'.format(self.filename))

        with open(self.filename) as f:
            self.settings = yaml.load(f, Loader=yaml.FullLoader)
            return self

    def save_settings(self, settings=None):

        """ Function model.settings.SettingsModel.save_settings.
        This function checks a dictionary of configurable values to be converted into the yaml file.
        If it's not possible, an exception is thrown.
        Arguments:
        settings -- an argument that stores the configurable values.
        """

        _settings = settings if settings else self.settings

        if not isinstance(_settings, dict):
            raise Exception('Invalid type')

        with open(self.filename, 'w') as f:
            return yaml.dump(_settings, f)

    def next_url(self):

        """ Function model.settings.SettingsModel.next_url.
        This function checks for feeds in the yaml file. If there are feeds, it loads them.
        If not, an exception is thrown.
        """     
           
        if 'feeds' in self.settings:
            if self._index not in range(0, len(self.settings['feeds'])):
                self._index = 0
            _url = self.settings['feeds'][self._index]
            self._index = self._index + 1
            return _url
        else:
            raise Exception("No feeds given.")
