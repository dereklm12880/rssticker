import View.rssticker as rssView
import Model.rssticker as rssModel


def execute():
    content = rssModel.get_rss_feeds()
    rssView.render(content)