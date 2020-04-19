from RSS.model.rssfeed import RssModel
from RSS.view.userinterface import RSSticker
import time
from RSS.model.settings import SettingsModel


class RssController:
    settings_model = None
    rssfeed_model = None

    def __init__(self):
        self.settings_model = SettingsModel()
        self.settings_model.load_settings()
        self.rssfeed_model = RssModel()

    def load_urls(self):
        try:
            return self.settings_model.settings['feeds']
        except Exception as e:
            raise Exception("Unable to load our settings: {}".format(e))

    def next_url(self):
        try:
            self.rssfeed.newsreel_index_pos = self.rssfeed.newsreel_index_pos + 1
            return self.list_urls[self.url_index_pos]
        except IndexError:
            raise Exception("There are no more URL's!")

    def next_feed(self, _url):
        _rss_view_object = RSSticker()
        _rss_model_object = RssModel().parse(_url)

        for _ in range(len(_rss_model_object.newsreel)):
            _newsreel = _rss_model_object.get_next()
            # TODO get the correct method to call
            # _rss_view_object.build_window()
            print(_newsreel.title, ':', _newsreel.link)
            time.sleep(self.cycle_time)

        return True

    def reset_url_index(self):
        self.url_index_pos = 0

    def next_index(self):
        self.url_index_pos = self.url_index_pos + 1

    def save_settings(self, settings):
        if len(self.settings_model.settings) == 0:
            self.settings_model.settings = settings
        else:
            for key in settings:
                self.settings_model.settings[key] = settings[key]

        self.settings_model.save_settings(self.settings_model.settings)

