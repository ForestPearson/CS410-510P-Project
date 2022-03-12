# test_interfaces.py
import unittest
#from chocan_admin_interface import *
import src.chocan_admin_interface
#from service_provider_interface import *
import src.service_provider_interface
#from service_provider_handler import *
import src.service_provider_handler

# service provider interface test functions

#def test_providerInterface_valid_selction(capfd):
  #serviceProviderInterface.input = lambda: '5'
  #src.service_provider_interface.serviceProviderInterface.input = lambda: '5'
  #src.service_provider_interface.serviceProviderInterface.providerInterface()
  #out, err = capfd.readouterr()
  #assert out == "Selection not valid!"
  #src.service_provider_interface.serviceProviderInterface.input = input
class TestAuthMethods(unittest.TestCase):
    def test_auth(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_admin(self):
        interface = src.chocan_admin_interface.adminInterface()
        #Test that add/remove menu is functioning
        self.assertAlmostEqual(interface.add_remove_menu(), None)
        #Test that the base adminHandler menu is functioning
        self.assertAlmostEqual(interface.admin_menu(), None)

if __name__ == '__main__':
    unittest.main()