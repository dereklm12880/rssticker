from pathlib import Path
import yaml
from os import path


class style_default(object):
    filename = str(Path(__file__).parents[2]) + '/settings.yaml'
    default_settings = ['white', 30, 'https://www.geeksforgeeks.org/python-check-if-all-elements-in-list-follow-a-condition/',
                                           '#000000','12pt','Times New Roman','top left']
    i=0

    def check_style(self):
        with open(self.filename) as file:
            settings_list = yaml.full_load(file)

        for item, value in settings_list.items():
            settings_list[item]
            if settings_list[item] is None:
                settings_list[item] = self.default_settings[self.i]
            self.i += 1
        print(settings_list)

        with open(self.filename, 'w') as file:
            try:
                settings_list = yaml.dump(settings_list, file)
            except yaml.YAMLError as exc:
                print(exc)



if __name__ == "__main__":
    style_default().check_style()




