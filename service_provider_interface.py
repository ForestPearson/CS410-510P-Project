from service_provider_handler import *

class serviceProviderInterface:
    def providerInterface(self, provId):
        handler = providerHandler()
        serviceProviderInterface.providerMainMenu(self)
        while True:
            selection = True
            selection = input("Your Selection: ")
            if selection == "1":
                handler.displayService()
                serviceProviderInterface.providerMainMenu(self) 
            elif selection == "2":
                handler.makeReport(provId)
                serviceProviderInterface.providerMainMenu(self) 
            elif selection == "3":
                handler.requestReport()
                serviceProviderInterface.providerMainMenu(self) 
            elif selection == "4":
                handler.deleteMemberReport()
                serviceProviderInterface.providerMainMenu(self)
            elif selection == "0":
                break
            else:
                print("Selection not valid!")

    def providerMainMenu(self):
        print("\nPlease enter the number corresponding to the service.\n")
        print("1. Display all services")
        print("2. Provide service")
        print("3. Request Report")
        print("4. Delete member report")
        print("0. Exit\n")
