import unittest
import src.login_handler

class TestAuthMethods(unittest.TestCase):
    def test_auth(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_valid_login(self):
        auth = src.login_handler.loginClass()
        #Test an invalid login for return -1
        self.assertEqual(auth.login("Not","Real"), -1)
        #Test a valid Admin login for no return
        self.assertEqual(auth.login("Hanks","passw0rd"), None)
        #Test a valid Provider login for no return
        self.assertEqual(auth.login("Bobbies","passw0rd"), None)
    
if __name__ == '__main__':
    unittest.main()