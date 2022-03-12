# test_auth.py
#import sys
#sys.path.insert(1, '/src')
import unittest
import src.auth
#from auth import *
# from login_handler import *
# from account_management import *
# from report_management import *
# from auth import *

class TestAuthMethods(unittest.TestCase):
    def test_auth(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
if __name__ == '__main__':
    unittest.main()
