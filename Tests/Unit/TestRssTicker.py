import unittest
from unittest import mock


class TestRssTicker(unittest.TestCase):

    def test_get_rss_feeds(self):
        with mock.patch('Model.rssticker') as mock_rss:
            mock_rss.get_rss_feeds.return_value = {
                'feed': {
                    'title': 'BBC News - Home'
                },
                'entries': [
                    {
                        'title': 'Coronavirus: Three days more sick pay for self-isolating workers',
                        'summary': 'Workers will get statutory sick pay from the first day off work, Boris Johnson tells the Commons.',
                        'link': 'https://www.bbc.co.uk/news/uk-51738837',
                    },
                    {
                        'title': 'Super Tuesday: Biden seals comeback with string of victories',
                        'summary': 'Joe Biden reverses recent setbacks as Democrats jostle to challenge Donald Trump for the White House.',
                        'link': 'https://www.bbc.co.uk/news/world-us-canada-51731293',
                    },
                ]
            }
            values = mock_rss.get_rss_feeds()
            assert values['feed']['title'] == 'BBC News - Home'
            assert values['entries'][0]['link'] == 'https://www.bbc.co.uk/news/uk-51738837'


if __name__ == '__main__':
    unittest.main()
