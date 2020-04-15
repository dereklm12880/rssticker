from RSS.model.rssfeed import RssModel
from RSS.view.userinterface import RSSticker
import csv
import time
import concurrent.futures
from pathlib import Path
from threading import Thread

class RssController:
    list_urls = []
    list_iterator = None
    rss_model = None
    rss_view = None
    url_index_pos = 0
    filename = ''
    cycle_time = 1

    def __init__(self):
        self.rss_model = RssModel()
        # self.rss_view = RssView
        self.filename = str(Path(__file__).parents[2]) + '/list_urls.csv'

    def load_urls(self):
        try:
            with open(self.filename, newline='') as f:
                reader = csv.reader(f)  # this CSV is in the controller folder
                self.list_urls = list(reader)
                self.list_iterator = iter(self.list_urls)
                return self.list_urls
        except FileNotFoundError:
            raise Exception("There is no file named " + self.filename + " in this directory")

    def next_url(self):

        if self.url_index_pos == 0:
            self.url_index_pos = self.url_index_pos + 1
            return self.list_urls[0]
        try:
            current_index = self.url_index_pos
            self.url_index_pos = self.url_index_pos + 1
            return self.list_urls[current_index]
        except IndexError:
            raise Exception("There are no more URL's!")

    def next_feed(self, _url):
        list_feeds = []
        _rss_model = self.rss_model.parse(_url[0])

        while self.rss_model._newsreel_index_pos < len(self.rss_model.newsreel):
                _newsreel = _rss_model.get_next()
                list_feeds.append(_newsreel)
                # TODO pass newsreel to the view
                print(_newsreel)
                time.sleep(self.cycle_time)

        return list_feeds

    def main(self):
        _feeds = []
        self.list_urls = self.load_urls()

        if len(self.list_urls) == 0:
            raise Exception("No URL's given")

        for _ in self.list_urls:
            # self.rss_model._newsreel_index_pos = 0
            _url = self.next_url()  # This gets the first url
            if not _feeds:
                _feeds = self.next_feed(_url)
            else:
                _feeds = _feeds + self.next_feed(_url)
                # Thread attempt where print is a stand in for the views method
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(print, _feeds)

if __name__ == "__main__":
    RssController().main()
