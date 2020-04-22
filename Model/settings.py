from pathlib import Path
import yaml
from os import path


class SettingsModel:
    filename = str(Path(__file__).parents[2]) + '/settings.yaml'
    settings = {}
    _index = 0


    def load_settings(self):
        if not path.exists(self.filename):
            raise Exception('No file exists {}'.format(self.filename))

        with open(self.filename) as f:
            self.settings = yaml.load(f, Loader=yaml.FullLoader)
            return self

    def save_settings(self, settings=None):
        _settings = settings if settings else self.settings

        if not isinstance(_settings, dict):
            raise Exception('Invalid type')

        with open(self.filename, 'w') as f:
            return yaml.dump(_settings, f)

    def next_url(self):
        if 'feeds' in self.settings:
            if self._index not in range(0, len(self.settings['feeds'])):
                self._index = 0
            _url = self.settings['feeds'][self._index]
            self._index = self._index + 1
            return _url
        else:
            raise Exception("No feeds given.")