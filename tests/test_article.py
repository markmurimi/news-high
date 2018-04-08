import unittest
from app.models import NewsArticles


class TestingNewsArticles(unittest.TestCase):
    '''
    Test class to test behaviours of the Article class
    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_article = NewsArticles('BBC News', 'EU acts against Poland judiciary reforms', 'Unprecedented disciplinary measures are taken as the EU says the reforms threaten the rule of law.',
                                    'https://ichef.bbci.co.uk/news/1024/cpsprodpb/F046/production/_98901516_2efffed4-d4a6-486a-8a78-112232b92faa.jpg', 'http://www.bbc.co.uk/news/world-europe-42420150', '2017-12-20T13:36:14Z')

    def test_instance(self):
        '''
        Test case to check if self.new_article is an instance of Article
        '''
        self.assertTrue(isinstance(self.new_article, NewsArticles))

    def test_init(self):
        '''
        Test case to check if the Article class is initialised
        '''
        self.assertEqual(self.new_article.author, 'BBC News')
        self.assertEqual(self.new_article.title,
                         'EU acts against Poland judiciary reforms')
        self.assertEqual(self.new_article.description,
                         'Unprecedented disciplinary measures are taken as the EU says the reforms threaten the rule of law.')
        self.assertEqual(self.new_article.urlToImage,
                         'https://ichef.bbci.co.uk/news/1024/cpsprodpb/F046/production/_98901516_2efffed4-d4a6-486a-8a78-112232b92faa.jpg')
        self.assertEqual(self.new_article.url,
                         'http://www.bbc.co.uk/news/world-europe-42420150')
        self.assertEqual(self.new_article.publishedAt, '2017-12-20T13:36:14Z')

if __name__=='__main__':
    unittest.main(verbosity=2)