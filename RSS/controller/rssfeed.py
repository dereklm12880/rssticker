import tkinter as tk
import os, sys
sys.path.append("../")
from RSS.controller import rssfeed as controller
from RSS.view import userinterface as ui
from RSS.model.rssfeed import RssModel
from RSS.model.settings import SettingsModel



class RssController:
    settings_model = None
    rssfeed_model = None

    def __init__(self):
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

if __name__ == "__main__":
    root = tk.Tk()
    window = ui.RSSticker(master=root)
    window.mainloop()