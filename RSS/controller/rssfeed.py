import tkinter as tk
import os, sys

sys.path.append("../")
from RSS.view import userinterface as ui
from RSS.model.rssfeed import RssModel
from RSS.model.settings import SettingsModel

class RssController(tk.Tk):
    settings_model = None
    rssfeed_model = None
    userinterface = None

    def __init__(self):
        super(RssController, self).__init__()
        self.settings_model = SettingsModel().load_settings()
        self.rssfeed_model = RssModel()

    def next_feed(self):
        try:
            return self.rssfeed_model.parse(self.settings_model.next_url())
        except Exception as e:
            raise e

    def save_settings(self, settings):
        if len(self.settings_model.settings) == 0:
            self.settings_model.settings = settings
        else:
            for key in settings:
                self.settings_model.settings[key] = settings[key]

        self.settings_model.save_settings(self.settings_model.settings)

    def render_view(self):
        _ui = ui.RSSticker(self)
        _ui.run_newsreel()
        _ui.mainloop()

"""See: https://stackoverflow.com/questions/23100704/running-infinite-loops-using-threads-in-python"""
if __name__ == "__main__":
    try:
        RssController().render_view()
    except Exception as e:
        """TODO add in a message that prompts the error."""
        print(e)


