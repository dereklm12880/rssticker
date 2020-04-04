from RSS.model.rssfeed import RssModel
# from RSS.view.rssticker import RssView # # This RssView is still unwritten as of now
import csv
import time


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
        self.filename = 'list_urls.csv'

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

    def main(self):

        self.list_urls = self.load_urls()
        if len(self.list_urls) == 0:
            raise Exception("No URL's given")
        try:
            _url = self.next_url()  # This gets the first url
        except StopIteration:
            raise Exception()
        try:
            while self.rss_model._newsreel_index_pos <= len(
                    self.rss_model.newsreel):  # This condition is a place holder for the condition that will be passed
                # from view (window closed)
                if self.rss_model._newsreel_index_pos == 0:
                        _rss_model = self.rss_model.parse(_url[self.url_index_pos - 1])
                        _newsreel = _rss_model.get_current()
                    # # pass newsreel into the view here
                        print(_newsreel)
                    # # sleep x number of seconds?
                        time.sleep(self.cycle_time)
                        _newsreel = _rss_model.get_next()
                # # do an infinite loop here
                else:
                    # # pass newsreel to the view
                    print(_newsreel)
                    # sleep x number of seconds
                    time.sleep(self.cycle_time)
                _newsreel = _rss_model.get_next()
                # return _newsreel
                # end infinite loop here. (no code needed)
        except Exception as e:
            # this needs to get the next url???
            # _url = self.next_url()
            pass
        # end first infinite loop (no code needed)


if __name__ == "__main__":
    RssController().main()
