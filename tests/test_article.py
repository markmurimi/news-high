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
        
    def test_instance(self):
        '''
       This test is to check 
        '''
        self.assertTrue(isinstance(self.new_article, NewsArticles))
    
    def test_init(self):
        '''
        Test case to check if the Article class is initialised
        '''
        
if __name__=='__main__':
    unittest.main(verbosity=2)