import tkinter as tk
import os, sys

sys.path.append("../")
from RSS.view import userinterface as ui
from RSS.model.rssfeed import RssModel
from RSS.model.settings import SettingsModel


class RssController():
  
    """ Class controller.rssfeed.RssController.
    This class customizes the Tkinter root window. It creates, displays, modifies
    and receives input from the controller.
    """

    settings_model = None
    rssfeed_model = None
    userinterface = None

    def __init__(self):
        super(RssController, self).__init__()
        """Constructor for controller.rssfeed.RssController."""
        self.settings_model = SettingsModel().load_settings()
        self.rssfeed_model = RssModel()

    def next_feed(self):
        """ Function controller.rssfeed.RssController.next_feed.
        This function returns the feeds parsed in the model, otherwise
        throwing an exception.
        """
        try:
            return self.rssfeed_model.parse(self.settings_model.next_url())
        except Exception as e:
            raise e

    def save_settings(self, settings):
        """ Function controller.rssfeed.RssController.save_settings.
        This saves function saves user choices such as font, background
        color, window placement, etc into the yaml file.
        Arguments:
        settings -- an argument that saves the settings.
        """
        if len(self.settings_model.settings) == 0:
            self.settings_model.settings = settings
        else:
            for key in settings:
                self.settings_model.settings[key] = settings[key]

        self.settings_model.save_settings(self.settings_model.settings)


if __name__ == "__main__":  # pragma: no cover
    try:
        _ui = ui.RSSticker(RssController())
        _ui.run_newsreel()
        _ui.mainloop()
    except Exception as e:
        print(e)
