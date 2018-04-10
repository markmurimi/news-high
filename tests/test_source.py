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
        
    def test_init(self):
        '''
        Test case to check if the NewsSource class is initialised
        '''
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
    
