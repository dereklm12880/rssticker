# method for rss links
import feedparser


class RssModel:
    _newsreel_index_pos = 0
    _raw_feed = ''

    given_url = ''
    title = ''
    subtitle = ''
    link = ''
    newsreel = []

    def parse(self, feed_url):
        if not isinstance(feed_url, str):
            raise Exception('Expects string {} given'.format(type(feed_url)))
        self._raw_feed = feedparser.parse(feed_url)
        if len(self._raw_feed) == 0:
            raise Exception("No feed with the url {} found.".format(feed_url))
        self.given_url = feed_url
        self.title = self._raw_feed['feed']['title']
        self.subtitle = self._raw_feed['feed']['subtitle']
        self.link = self._raw_feed['feed']['link']
        self.newsreel = self._raw_feed['entries']
        return self

    def get_current(self):
        try:
            return self.newsreel[self._newsreel_index_pos]
        except IndexError:
            raise Exception("There is no news loaded! Try parsing a new RSS feed.")

    def get_next(self):
        try:
            self._newsreel_index_pos = self._newsreel_index_pos +1
            return self.newsreel[self._newsreel_index_pos]
        except IndexError:
            raise Exception("There is no more news! Try parsing a new RSS feed.")
