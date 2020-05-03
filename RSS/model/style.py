from pathlib import Path
import yaml
# sys.path.append("../../")
from RSS.controller.rssfeed import RssController


class style_default(object):
    filename = str(Path(__file__).parents[2]) + '/settings.yaml'
    default_settings = ['white', 30,
                        'https://www.geeksforgeeks.org/python-check-if-all-elements-in-list-follow-a-condition/',
                        '#000000', '12pt', 'Times New Roman', 'top left']
    default = ['#000000', 'top left', 5]

    i = 0

    def load_settings(self):
        # if not path.exists(self.filename):
        #     raise Exception('No file exists {}'.format(self.filename))

        with open(self.filename) as file:
            settings_list = yaml.full_load(file)
        return settings_list

    def check_style(self):
        settings_list = self.load_settings()

        for item, value in settings_list.items():
            settings_list[item]
            if settings_list[item] is None:
                settings_list[item] = self.default_settings[self.i]
            self.i += 1
        return settings_list

    def check_dump(self, dictionary):
        dictionary = style_default().check_style()
        with open(self.filename, 'w') as file:
            try:
                return yaml.dump(dictionary, file)
                print(dictionary)
            except yaml.YAMLError as exc:
                print(exc)

        self.popup_window.geometry("200×100")


if __name__ == "__main__":
    # style_default().check_dump(style_default().check_style())
    style_default().save('white', 'top left', 5)
