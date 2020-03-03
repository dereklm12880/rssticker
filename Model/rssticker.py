import feedparser


def getRssFeeds():
    python_wiki_rss_url = "http://www.python.org/cgi-bin/moinmoin/" \
                          "RecentChanges?action=rss_rc"
    bbc_news = "http://feeds.bbci.co.uk/news/rss.xml"
    return feedparser.parse(bbc_news)
