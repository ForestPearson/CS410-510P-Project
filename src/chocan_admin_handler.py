# This component of the controller will manage all service
# provider requests. This includes: login requests, provider
# and member account updates

#from login_handler import *
import src.login_handler
#from report_generation_handler import *
import src.report_interface
import src.account_management

class adminHandler:

    #####
    # Update any account
    #####
    def updateAcct(self) -> int:

        #acctMgr = src.accountManager()
        acctMgr = src.account_management.accountManager()
        kbinput = ""
        while not kbinput.isnumeric():
            kbinput = input("Enter the member ID: ")

        acct = acctMgr.getAccountById(int(kbinput))

        if acct == -1:
            print("No matching ID")
            return -1

        kbinput = "x"

        while not kbinput.isnumeric() or int(kbinput) < 1 or int(kbinput) > 8:
            kbinput = input("""
                  Enter the number of the field to change:
                  1. Name
                  2. Phone
                  3. Address
                  4. Username
                  5. Password
                  6. Account Type
                  7. Additional Info
                  8. Exit
                  """)

        # Update Member Account
        match int(kbinput):
            # For any acct type
            case 1:  # Name
                print(f'Old value: {acct["name"]}, new: ')
                acctMgr.updateAccount(acct["id"], name=input())
            case 2:  # Phone
                print(f'Old value: {acct["phone"]}, new: ')
                acctMgr.updateAccount(acct["id"], phone=input())
            case 3:  # Address
                print(f'Old value: {acct["address"]}, new: ')
                acctMgr.updateAccount(acct["id"], address=input)
            case 4:  # Username
                print(f'Old value: {acct["username"]}, new: ')
                acctMgr.updateAccount(acct["id"], username=input())
            case 5:  # Password
                print(f'Old value: {acct["password"]}, new: ')
                acctMgr.updateAccount(acct["id"], password=input)
            case 6:  # Account Type
                print(f'Old value: {acct["type"]}, new: ')
                acctMgr.updateAccount(acct["id"], type=input())
            # Per acct type attributes
            case 7:  # Additional Info
                if acct["type"] == "member":  # MEMBER SPECIFIC ATTRIBUTES
                    kbinput = ""
                    while not kbinput.isnumeric() or int(kbinput) < 1 or int(kbinput) > 7:
                        kbinput = input("""
                      Enter the number of the field to change:
                      1. Status
                      2. Services
                      """)
                    match int(kbinput):
                        case 1:
                            print(f'Old value: {acct["status"]}, new: ')
                            acctMgr.updateAccount(acct[1], status=input())
                        case 2:
                            print(f'Old value: {acct["services"]}, new: ')
                            acctMgr.updateAccount(acct[1], services=input)
                if acct["type"] == "provider":   # PROVIDER SPECIFIC ATTRIBUTES
                    print(
                        f'Services offered:\nOld value: {acct["offered"]}, new: ')
                    acct["offered"] = input()
                    acctMgr.updateAccount(acct[1], acct)
            case 8:  # Exit
                print(f'Exit')
        return 1

    #####
    # Create new account for any type
    #####

    def addAcct(self) -> int:

        #acctmgr = src.accountManager()
        acctMgr = src.account_management.accountManager()
        name = ""
        phone = ""
        address = ""
        username = ""
        password = ""
        type = ""
        status = ""
        offered = ""

        # Generate account with inputed information
        # ID genertated in account_magement by makeAccount()
        name = input("Enter the name: ")
        phone = ""
        phone = input("Enter the phone number: ")
        while (not phone.isnumeric() or len(phone) != 10):
            # Only numeric phone numbers with a lenth of 10.
            phone = input("Please enter a valid 10 digit phone number: ")
        address = input("Enter the address: ")
        username = name.strip()
        # Ensure the username is name w/o spaces
        password = input("Enter secure passord: ")
        type = ""
        while (type != "admin" and type != "member" and type != "provider"):
            type = input(
                "Type of account (admin/provider/member): ").casefold()
        if type == "member":
            status = input("Member status (active/inactive): ")
            try:
                acctMgr.makeAccount(name=name, phone=phone, address=address, username=username,
                                    password=password, type=type, status=status, services="")
            except:
                print("error accessing db to create account")
                return -1
        if type == "provider":
            offered = input("Services Offered: ").split()
            try:
                acctMgr.makeAccount(name=name, phone=phone, address=address, username=username,
                                    password=password, type=type, services=offered, offered="")
            except:
                print("error accessing db to create account")
                return -1
        if type == "admin":
            try:
                acctMgr.makeAccount(name=name, phone=phone, address=address, username=username,
                                    password=password, type=type, services=offered, offered="")
            except:
                print("error accessing db to create account")
                return -1
        return 1

    #####
    # Calls delete account method from accountManager
    #####

    def delAcct(self) -> int:

        #acctMgr = src.accountManager()
        acctMgr = src.account_management.accountManager()

        kbinput = ""
        verify = ""
        kbinput = input("Enter the member ID: ")
        while not kbinput.isnumeric():
            kbinput = input("Enter a numeric member ID: ")
        while (verify != "Y" and verify != "N"):
            verify = input("Please Enter Y/N to confrim deletion: ")
        if verify == "Y":
            if acctMgr.delAccount(kbinput) == -1:
                print("Nothing deleted, invalid ID")
                return -1
            print(f"account {kbinput} purged")
        if verify =="N":
          print("Deletion cancelled")
        return 1

    #####
    # Run weekly report request.  Provides the following reports:
    #   For each provider: weekly report of services provided & total due
    #   For each member: weekly report of services received
    #   AP report for total billable weekly services by provider
    #####

    def generateReports(self, admID) -> int:
        #reports = src.reportHandler()
        #reports = src.report_generation_handler.reportHandler()
        reports = src.report_interface.report_menu(admID)
        #print("Generating the weekly reports...")
        # Call methods from report handler to create report files...
        #reports.makePayableReport("")
        #reports.displayPayableReport()
        print("Reports dispersed.")
        return 1
