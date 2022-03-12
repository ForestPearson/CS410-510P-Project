#This file will display a menu interface for the type of report to be generated.
#Types of reports can be: a list of services, payable report, member report, and provider report.

from src.report_generation_handler import *


def report_choices(self, num):
    handler = reportHandler()

    if num == 1:
        print (23 * "-" , "Weekly Payable Reports Interface" , 23 * "-")
    elif num == 2:
        print (23 * "-" , "Member Reports Interface" , 23 * "-")
    elif num == 3:
        print (23 * "-" , "Provider Reports Interface" , 23 * "-")

    loop = True

    while loop:
        print("""
             1. Create Report
             2. Display Report
             3. Delete Report
             4. Quit""")
        print (65 * "-" + "\n")
            
        choice = input("Enter choice [1-4]: ")

        
        if choice == "1":
            if num == 1:
                #Generates weekly payable report
                print("Creating payable weekly report")
                handler.makePayableReport()
            elif num == 2:
                #Generates member report
                print("Go to create member report")
            elif num == 3:
                #Generates provider report
                print("Go to create provider report")

        elif choice == "2":
            if num == 1:
                #Display weekly payable report
                print("Display weekly report")
            elif num == 2:
                #Display member report
                print("Display member report")
            elif num == 3:
                #Display provider report
                print("Display provider report")

        elif choice == "3":
            if num == 1:
                #Deletes weekly payable report
                print("Remove payable weekly report")
            elif num == 2:
                #Remove member report
                print("Remove member report")
            elif num == 3:
                #Remove provider report
                print("Remove provider report")
                
        elif choice == "4":
            break
        else:
            print("Wrong selection. Enter 1-4 and try again")

def report_menu(self):

        print (23 * "-" , "Report Generation Interface" , 23 * "-")

        loop = True

        while loop:
            print("""
                 1. Weekly Payable Reports
                 2. Member Reports
                 3. Provider Reports
                 4. Quit""")
            print (65 * "-" + "\n")
            
            choice = input("Enter choice [1-4]: ")

            if choice == "1":
                #Calls weekly payable report menu
                adminInterface.add_remove_menu(self)
            elif choice == "2":
                print ("Change Provider Information")
                handler.updateAcct()
            elif choice == "3":
                print ("Remove Service provider")
                handler.delAcct()
            elif choice == "4":
                break
            else:
                print("Wrong selection. Enter 1-4 and try again")