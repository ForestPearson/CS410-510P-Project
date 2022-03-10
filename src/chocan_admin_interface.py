# Chocoan Admin Interface Viewer.
# Menu with included functions
#   1. Add, remove and modify account information
#   2. Change Provider Information
#   3. Add/Remove Service provider
#   4. Request Report
#   5. Request Service Directory
# Must have home screen

#from chocan_admin_handler import *
import src.chocan_admin_handler

class adminInterface:

    # This is the main menu for adjusting account information
    # Allows add, modify, and remove. Works with admin handler file
    def add_remove_menu(self):
        #handler = src.adminHandler()
        handler = src.chocan_admin_handler.adminHandler()

        user_input = True

        while user_input:
            print (22 * "-" , "Add/Remove/Modify" , 22 * "-")
            print ("""
                  1. Add Account
                  2. Modify Account
                  3. Remove Account""")
            print (65 * "-" + "\n")
            user_input = input("Enter choice [1-3]: ")

            if user_input == "1":
                #Adds account to json through handler
                handler.addAcct()
            elif user_input == "2":
                #Updates accounts to json through handler
                handler.updateAcct()
            elif user_input == "3":
                #Delete account to json through handler
                handler.delAcct()
            else:
                print("Try Again")

    def admin_menu(self):
        #handler = src.adminHandler()
        handler = src.chocan_admin_handler.adminHandler()
        print (23 * "-" , "Admin Interface" , 23 * "-")

        loop = True

        while loop:
            print("""
                 1. Add, Modify and Remove account information
                 2. Change Provider Information
                 3. Remove Service provider
                 4. Request Weekly Report
                 5. Quit""")
            print (65 * "-" + "\n")
            
            choice = input("Enter choice [1-5]: ")

            if choice == "1":
                #Calls add/modify/remove account menu definition
                adminInterface.add_remove_menu(self)
            elif choice == "2":
                print ("Change Provider Information")
                handler.updateAcct()
            elif choice == "3":
                print ("Remove Service provider")
                handler.delAcct()
            elif choice == "4":
                #Calls handler report call
                handler.weeklyReports()
            elif choice == "5":
                break
            else:
                print("Wrong selection. Enter 1-5 and try again")