import feedparser


def get_rss_feeds():
    bbc_news = "http://feeds.bbci.co.uk/news/rss.xml"
    return feedparser.parse(bbc_news)
