from RSS.model.rssfeed import RssModel
from RSS.view.userinterface import RSSticker
import time
from RSS.model.settings import SettingsModel


class RssController:
    list_urls = []
    list_iterator = None
    url_index_pos = 0
    cycle_time = 3
    settings_model = None

    def __init__(self):
        self.settings_model = SettingsModel().load_settings()
        self.cycle_time = self.settings_model.settings['cycle_time'][0] if self.settings_model.settings[
            'cycle_time'] else self.cycle_time

    def load_urls(self):
        return self.settings_model.load_settings().settings['feeds']

    def next_url(self):
        try:
            self.url_index_pos = self.url_index_pos + 1
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

    def run(self):
        # for _url in self.list_urls:
        # while True:
        # TODO make custom exceptions, one for the feed model _out of news_ and another for the view
        for _ in range(10):
            if self.url_index_pos == len(self.list_urls):
                self.reset_url_index()
            # print(self.url_index_pos)
            # print(self.list_urls[self.url_index_pos])
            # print(len(self.list_urls))
            try:
                self.next_feed(self.list_urls[self.url_index_pos])
            except Exception as e:
                print(e)
            finally:
                self.next_index()

    def main(self):
        try:
            self.list_urls = self.load_urls()
        except Exception:
            self.list_urls = None

        if not self.list_urls or len(self.list_urls) == 0:
            # FIXME send a message to the view that we have no Feeds to display NOT an exception.
            raise Exception("No URL's given")
        else:
            self.run()  # We can leverage the loop here and code coverage might get better.


if __name__ == "__main__":
    RssController().main()
