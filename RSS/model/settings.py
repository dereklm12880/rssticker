from pathlib import Path
import yaml
from os import path


class SettingsModel:
    filename = str(Path(__file__).parents[2]) + '/settings.yaml'
    settings = {}

    def load_settings(self):
        if not path.exists(self.filename):
            raise Exception('No file exists {}'.format(self.filename))

        with open(self.filename) as f:
            self.settings = yaml.load(f, Loader=yaml.FullLoader)
            return self

    def save_settings(self, settings=None):
        _settings = settings if settings else self.settings

        with open(self.filename, 'w') as f:
            return yaml.dump(_settings, f)
