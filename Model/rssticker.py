import feedparser

class RssModel:
    def get_rss_feeds(feed):
        return feedparser.parse(feed)
