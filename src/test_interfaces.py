# test_interfaces.py

from chocan_admin_interface import *
from service_provider_interface import *
from service_provider_handler import *

# service provider interface test functions

def test_providerInterface_valid_selction(capfd):
  serviceProviderInterface.input = lambda: '5'
  serviceProviderInterface.providerInterface()
  out, err = capfd.readouterr()
  assert out == "Selection not valid!"
  serviceProviderInterface.input = input
