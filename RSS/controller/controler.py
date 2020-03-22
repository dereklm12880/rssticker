
from RSS.model.rssfeed import RssModel
# from RSS.view.rssticker import RssView ##This RssView is still unwritten as of now
import csv
import time


class RssController:

    list_urls = []
    list_iterator = None
    rss_model = None
    rss_view = None

    def __init__(self):
        self.rss_model = RssModel
        # self.rss_view = RssView

    def load_urls(self):
        with open('list_urls.csv', newline='') as f:
            reader = csv.reader(f)  # this CSV is in the controller folder
            self.list_urls = list(reader)
            self.list_iterator = iter(self.list_urls)
            list_urls = list(self.list_iterator)
            print(list_urls)
            return list_urls

    def next_url(self):
        return next(self.list_iterator)

    def main(self):
        self.load_urls()

        try:
            _url = self.next_url()

        except StopIteration: 
            _url = None
            pass
        try:
            if self.rss_model._newsreel_index_pos == 0:
                _rss_model = self.rss_model.parse(_url)
                _newsreel = self._rss_model.get_current()
                # # pass newsreel into the view here
                # self.rss_view(_newsreel)
                # # sleep x number of seconds?
                time.sleep(5)
                # # do an infinite loop here
            else:
                _newsreel = self._rssmodel.get_next()
                # # pass newsreel to the view
                # self.rss_view(_newsreel)
                # sleep x number of seconds
                time.sleep(5)
                return _newsreel
                # end infinite loop here. (no code needed)

        except Exception as e:
            # this needs to get the next url???
            #RssController.next_url(self)
            pass
        # end first infinite loop (no code needed)

    def next_url_fail(self):

        if self.next_url() == []:
            raise Exception("There are no new URL's!")

    def load_file_fail(self):
        if self.load_urls() == []:
            raise Exception("This file could not be loaded!")


if __name__ == "__main__":
    RssController().main()

    # list_urls = load_urls(self=list_urls)
    # next_url = next_url(list_urls)
    # print(list_urls)
    # print(next_url)