import View.rssticker as rssView
import Model.rssticker as rssModel


def execute():
    content = rssModel.getRssFeeds()
    rssView.render(content)