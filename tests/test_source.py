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


    
