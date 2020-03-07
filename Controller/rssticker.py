from View.rssticker import RssView
from Model.rssticker import RssModel


class RssController:
    def execute():
        bbc_news = "http://feeds.bbci.co.uk/news/rss.xml"

        content = RssModel.get_rss_feeds(bbc_news)
        RssView.render(content)
