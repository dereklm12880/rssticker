# To use feed parser you must import it: from RSS.model.rssfeed import RssModel.
# From there, you can then instantiate the class object and parse a url feed. e.g.
# @example {
# rss = new RssModel()
# news = rss.parse('http://someurl.com').get_current()
# }
# As time passes, you can load the next feed by simply calling the get_next() method.
# @example{
# try:
#   rss.get_next()
# except Exception as e:
#   print e
# }
# Exceptions are thrown when the following occurs:
# 1) No news feed is loaded, maybe invalid url or a timeout occurred.
# 2) No newsreel entities are found.. no clue why this would happen but plan for the worst--hope for the best.
# 3) Out of bounds (ran out of newsreel entities) and time to get more.
