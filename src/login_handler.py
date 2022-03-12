#from account_management import *
import src.account_management
#from service_provider_interface import *
import src.service_provider_interface
#from chocan_admin_interface import *
import src.chocan_admin_interface

class loginClass:
    def login(self, username, password):
        #manager = src.accountManager()
        manager = src.account_management.accountManager()
        account = manager.getAccountByUsername(username)

        if account == -1:
            return -1

        if account['password'] == password:
            if account['type'] == "member":
                return -1
            elif account['type'] == "provider":
                #provider = src.serviceProviderInterface()
                provider = src.service_provider_interface.serviceProviderInterface()
                provider.providerInterface(account['id'])
            elif account['type'] == "admin":
                #admin = src.adminInterface()
                admin = src.chocan_admin_interface.adminInterface()
                admin.admin_menu(account['id'])
        else:
            return -1