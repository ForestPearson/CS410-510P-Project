from account_management import *
from service_provider_interface import *
from chocan_admin_interface import *

class loginClass:
    def login(self, username, password):
        manager = accountManager()
        account = manager.getAccountByUsername(username)

        if account == -1:
            return -1

        if account['password'] == password:
            if account['type'] == "member":
                return -1
            elif account['type'] == "provider":
                provider = serviceProviderInterface()
                provider.providerInterface(account['id'])
            elif account['type'] == "admin":
                admin = adminInterface()
                admin.admin_menu()
        else:
            return -1