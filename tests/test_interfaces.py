# test_interfaces.py

#from chocan_admin_interface import *
import src.chocan_admin_interface
#from service_provider_interface import *
import src.service_provider_interface
#from service_provider_handler import *
import src.service_provider_handler

# service provider interface test functions

def test_providerInterface_valid_selction(capfd):
  #serviceProviderInterface.input = lambda: '5'
  src.service_provider_interface.serviceProviderInterface.input = lambda: '5'
  src.service_provider_interface.serviceProviderInterface.providerInterface()
  out, err = capfd.readouterr()
  assert out == "Selection not valid!"
  src.service_provider_interface.serviceProviderInterface.input = input
