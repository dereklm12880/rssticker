from pathlib import Path
import yaml
from os import path


class style_default(object):
    filename = str(Path(__file__).parents[2]) + '/settings.yaml'
    default_settings = ['white', 30,
                        'https://www.geeksforgeeks.org/python-check-if-all-elements-in-list-follow-a-condition/',
                        '#000000', '12pt', 'Times New Roman', 'top left']
    i = 0
    with open(filename) as file:
        settings_list = yaml.full_load(file)
        print(settings_list)

    def check_style(self):
        settings_list = self.settings_list
        for item, value in settings_list.items():
            settings_list[item]
            if settings_list[item] is None:
                settings_list[item] = self.default_settings[self.i]
            self.i += 1
        return settings_list
        print(settings_list)

    def check_dump(self):
        with open(self.filename, 'w') as file:
            try:
                # self.settings_list = yaml.dump(settings_list, file)
                return yaml.dump(self.settings_list, file)
            except yaml.YAMLError as exc:
                print(exc)


if __name__ == "__main__":
    style_default().check_style()
    style_default().check_dump()


