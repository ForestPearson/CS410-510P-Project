#This file will display a menu interface for the type of report to be generated.
#Types of reports can be: Payable report, member report, and provider report.
#This functionality is only utilized by Admins. 
#If Providers want to use functionality, we need to allow specific accesses that are not yet implemented in this file.

from src.report_generation_handler import *
from datetime import date

#Sub menu to allow functionality based on the type of report sent in from main menu.
def report_choices(num, admID):
    handler = src.report_generation_handler.reportHandler()
    loop = True

    while loop:
        if num == "1":
            print ("\n", 23 * "-" , "Weekly Payable Reports Interface" , 23 * "-")
        elif num == "2":
            print ("\n", 23 * "-" , "Member Reports Interface" , 23 * "-")
        elif num == "3":
            print ("\n", 23 * "-" , "Provider Reports Interface" , 23 * "-")
        print("""
             1. Create Report
             2. Display Report
             3. Delete Report
             4. Go Back""")
        print (65 * "-" + "\n")
            
        choice = input("Enter choice [1-4]: ")

        #This will create reports and will use num to create specificed reports.
        if choice == "1":
            #Date to send in when report was created.
            today = date.today()
            d1 = today.strftime("%m/%d/%y")

            if num == "1":
                #Generates payable weekly reports.
                #This functionality is only allowed to Admins.
                print("\nCreating payable weekly report...")
                handler.makePayableReport(d1)
            elif num == "2":
                #Generates member report utilizing a member ID and service ID (for a service being provided to them).
                #This functionality is allowed to Admins and Providers.
                memberId = int(input("Enter member ID: "))
                servId = int(input("Enter service ID: "))
                print("\nCreating member report...")
                handler.makeMemberReport(memberId, admId, servId, d1)
            elif num == "3":
                #Generates provider report utilizing a provider ID.
                #This functionality is allowed only to Admins.
                provId = int(input("Enter provider ID: "))
                print("\nCreating provider report...")
                handler.makeProviderReport(provID, d1)

        #This will display reports and will use num to display specificed reports.
        elif choice == "2":
            #Functionality will allow all reports to be displayed or only a specific one.
            res = input("Would you like to display a specific report?[Y/N] (N = all reports are printed): ")
            if num == "1":
                #Displays weekly payable report.
                #This functionality is only allowed to Admins.
                if(res.upper() == 'N'):
                    #Display all reports.
                    print("Displaying all payable weekly reports...")
                    handler.displayPayableReport()
                else:
                    #Display single report from ID.
                    repid = input("Enter report ID of the report you'd like to access: ")
                    print("Displaying payable weekly report #",repid,"...")
                    handler.displayPayableReport(repid)
            elif num == "2":
                #Display member report.
                #This functionality is allowed to Admins and Providers.
                if(res.upper() == 'N'):
                    #Display all reports.
                    print("Displaying all member reports...")
                    handler.displayMemberReport()
                else:
                    #Display single report from ID.
                    repid = input("Enter report ID of the report you'd like to access: ")
                    print("Displaying member report #",repid,"...")
                    handler.displayMemberReport(repid)
            elif num == "3":
                #Display provider report.
                #This functionality is only allowed to Admins.
                if(res.upper() == 'N'):
                    #Display all reports.
                    print("Displaying all provider reports...")
                    handler.displayProviderReport()
                else:
                    #Display single report from ID.
                    repid = input("Enter report ID of the report you'd like to access: ")
                    print("Displaying provider report #",repid,"...")
                    handler.displayProviderReport(repid)

        #This will delete reports and will use num to delete specificed reports.
        elif choice == "3":
            res = input("Would you like to access a specific report?[Y/N] (if N, all reports are deleted): ")
            if num == "1":
                #Delete weekly payable report.
                #Functionality only allowed to Admins.
                if(res.upper() == 'N'):
                    #Deletes all weekly payable reports.
                    print("Removing all payable weekly reports...")
                    handler.delPayableReport()
                else:
                    repid = input("Enter report ID of the report you'd like to delete: ")
                    #Deletes single specified weekly payable reports.
                    print("Removing payable weekly report #",repid,"...")
                    handler.delPayableReport(repid)
            elif num == "2":
                #Delete member report.
                #Functionality allowed to Admins and Providers.
                if(res.upper() == 'N'):
                    #Deletes all member reports.
                    print("Removing all member reports...")
                    handler.delMemberReports()
                else:
                    #Deletes single specificed member report.
                    repid = input("Enter report ID of the report you'd like to delete: ")
                    print("Removing member report #",repid,"...")
                    handler.delMemberReports(repid)
            elif num == "3":
                #Delete provider report.
                #Functionality only allowed to Admins.
                if(res.upper() == 'N'):
                    #Deletes all provider reports.
                    print("Removing all provider reports...")
                    handler.delProviderReports()
                else:
                    #Deletes single specified provider report.
                    repid = input("Enter report ID of the report you'd like to delete: ")
                    print("Removing provider report #",repid,"...")
                    handler.delProviderReports(repid)
        #Exit the menu and go back to main menu to allow another selection.
        elif choice == "4":
            break
        else:
            print("Wrong selection. Enter 1-4 and try again")

#Main menu interface to choose the type of report that wants to be manipulated and accessed.
def report_menu(admID):
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

            if choice == "1" or choice == "2" or choice == "3":
                #Calls weekly payable report menu.
                report_choices(choice, admID)
            elif choice == "4":
                break
            else:
                print("Wrong selection. Enter 1-4 and try again")