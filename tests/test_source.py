import unittest
from app.models import NewsSources

class TestingNewsSources(unittest.TestCase):
    """Test to test the behaviour of the NewsSource class
    Args:
        unittest.Testcase : Test case class that helps create test cases"""

    def test_instance(self):
        """This is the test case to check the instance oof NewsSource"""
        
        self.assertTrue( isinstance( self.news_source, NewsSources ) )

    def setUp(self):
        """ Set up method to run before each test case """
        self.news_source = NewsSources('abc-news-au', 'ABC News (AU)',
                                   'Australia\'s most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.', "http://www.abc.net.au/news", "general")

    def test_init(self):
        '''
        Test case to check if the NewsSource class is initialised
        '''
        self.assertEqual(self.news_source.id, 'abc-news-au')
        self.assertEqual(self.news_source.name, 'ABC News (AU)')
        self.assertEqual(self.news_source.description,
                         'Australia\'s most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.')


if __name__ == '__main__':
    unittest.main(verbosity=2)
    
