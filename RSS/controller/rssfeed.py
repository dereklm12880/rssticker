from RSS.model.rssfeed import RssModel
from RSS.view.userinterface import RSSticker
import csv
import time
import concurrent.futures
from pathlib import Path


class RssController:
    list_urls = []
    list_iterator = None
    url_index_pos = 0
    filename = ''
    cycle_time = 0

    def __init__(self):
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
        try:
            self.url_index_pos = self.url_index_pos + 1
            return self.list_urls[self.url_index_pos]
        except IndexError:
            raise Exception("There are no more URL's!")

    def next_feed(self, _url):
        # TODO initiate view here
        _rss_model_object = RssModel().parse(_url)

        for _ in range(len(_rss_model_object.newsreel)):
            _newsreel = _rss_model_object.get_next()
            # TODO pass newsreel to the view
            print(_newsreel.title,':', _newsreel.link)
            time.sleep(self.cycle_time)

        return True

    def reset_url_index(self):
        self.url_index_pos = 0

    def next_index(self):
        self.url_index_pos = self.url_index_pos + 1

    def main(self):
        _feeds = []
        self.list_urls = self.load_urls()

        if len(self.list_urls) == 0:
            raise Exception("No URL's given")

        # for _url in self.list_urls:
        # while True:
        for _ in range(10):
            if self.url_index_pos == len(self.list_urls):
                self.reset_url_index()
            # print(self.url_index_pos)
            # print(self.list_urls[self.url_index_pos])
            # print(len(self.list_urls))
            try:
                self.next_feed(self.list_urls[self.url_index_pos][0])
            except Exception as e:
                print(e)
            finally:
                self.next_index()

        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     executor.submit(print, _feeds)

if __name__ == "__main__":
    RssController().main()
