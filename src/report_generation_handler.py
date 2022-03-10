#from report_management import reportManager
import src.report_management
#from account_management import accountManager
import src.account_management
class reportHandler:
  # From report_management.py to access members of reportManager class.
  #rm = src.reportManager
  rm = src.report_management
  # From account_management.py to access members of accountManager class.
  #am = src.accountManager
  am = src.account_management


  ############################## Services Management ############################## 

  #Add new service passed in by the other controllers to database.
  def addService(self, serviceName, cost):

    # Required fields to assemble service object:
    #   Service name
    #   Service ID
    #   Cost
    #-----------------------

    # Make sure fields are correctly formatted
    error = 0
    try:
      # If comparison is valid but values are invalid
      if cost < 0 or len(serviceName) == 0:
        error = -1
    except:
        error = -1
    
    if error == -1:
        print("\nError: Cannot add service\nReason: Fields are not formatted correctly.")
        print("\nExpected fields")
        print("---------------") 
        print("Name: String of characters.")
        print("Cost: Must be a number greater than or equal to zero.")
        return -1
    
    #return self.rm.addService(self.rm, serviceName, cost)
    return self.rm.reportManager.addService(self.rm, serviceName, cost)
        

  # Display services based on service code passed in by other controllers.
  # Display all services if no code specified.
  def displayServices(self, serviceCode=0):

    reports = []
    #reports = self.rm.getService(self.rm)
    reports = self.rm.reportManager.getService(self.rm)

    # Cannot open services.JSON or is empty.
    if reports == -1:
      print("\nNo services saved.")
      return -1

    # Iterate through the list of services.
    # Print all services if no serviceCode is provided.
    count = 0
    for entry in reports:
      if serviceCode == entry["id"] or serviceCode == 0:
        print("\nService Name: ", entry["name"])
        print("Service Code: ", entry["id"])
        print("Cost of Service: ", entry["cost"])
        count +=1

        # Only iterate until match is found
        if serviceCode != 0:
          break
    
    if count == 0:
      print("\nNo match found. Please enter a valid service code.")
      return 0

    return 1

  # Delete service associated with passed in service code or delete all services by default.
  def delService(self, serviceCode=0):

    #flag = self.rm.delService(self.rm, serviceCode)
    flag = self.rm.reportManager.delService(self.rm, serviceCode)

    if flag == -2:
      print("No services exist. Cannot delete already empty list of services.")
    elif flag == -1:
      print("All services deleted.") 
    elif flag == 0:
      print("No service exists with the service code #", serviceCode, " provided.")
    else:
      print("Service code #", serviceCode, "deleted.")
    
    return flag


  ############################## Member Reports Management ############################## 


  # Construct the fields required for a member report and pass these fields into the report model.
  # Must be called after member and service provider have been added to the accounts model.
  def makeMemberReport(self, memberId, provId, servId, date):

    # Required fields to assemble member report:
    #   Member ID
    #   Provider ID
    #   Service ID
    #   Date
    #-----------------------

    reports = self.rm
    accounts = self.am

    # Collect associated member info.
    #member = accounts.getAccountById(accounts, memberId)
    member = accounts.accountManager.getAccountById(accounts, memberId) 
    if member == -1 or member["type"] != "member":
      print("Invalid member ID. Cannot create member report.")
      return -1

    # Collect service provider info.
    #provider = accounts.getAccountById(accounts, provId)
    provider = accounts.accountManager.getAccountById(accounts, provId)
    if provider == -1 or provider["type"] != "provider":
      print("Invalid provider ID. Cannot create member report")
      return -1
    
    # Collect service info.
    #service = reports.getService(reports, servId)
    service = reports.reportManager.getService(reports, servId)
    # Display error message if specific service does not exist or none exist.
    if service == -1:
      print("No services saved. Cannot create member report.")
      return -1
    elif service == 0:
      print("Invalid service code. Cannot create member report.")
      return 0

    # Function call to the makeMemberReport function from report_management.py
    #return reports.makeMemberReport(reports, member, provider, service, date)
    return reports.reportManager.makeMemberReport(reports, member, provider, service, date)


  # Display member reports associated with the passed member ID or report ID.
  # Display all if no arguments given.
  # Return fail if no match is found. Does not display report ID as it is arbitrary.
  def displayMemberReport(self, memberId=0, reportId=0):
    
    reports = []
    #reports = self.rm.getMemberReports(self.rm)
    reports = self.rm.reportManager.getMemberReports(self.rm)

    #Check if member report exists.
    if reports == -1:
      print("No member reports saved. Cannot display member reports.")
      return -1

    flag = 0
    for entry in reports:
      if entry["member id"] == memberId or entry["report id"] == reportId or (memberId == 0 and reportId == 0):

        #Only display this info once, unless displaying all entries.
        if flag == 0 or (memberId == 0 and reportId == 0):
          flag = 1
          print("\nName:", entry["member name"])
          print("Member ID:", entry["member id"])
        
        #Print each received service.
        print("Service received on", entry["date"], ":", entry["service"])
        print("Service provider:", entry["provider name"])
        print("Cost: $", entry["cost"])
        print("Report ID:", entry["report id"], "\n")
    
    if flag == 0:
      print("\nInvalid report and/or member IDs supplied. Cannot generate member report.")
      return 0
    
    return 1


  #Delete all member reports associated with passed in memberID or all by default.
  def delMemberReports(self, memberId=0, reportId=0):

    #flag = self.rm.delMemberReports(self.rm, memberId, reportId)
    flag = self.rm.reportManager.delMemberReports(self.rm, memberId, reportId)

    #No member reports saved.
    if flag == -2:
      print("No member reports saved. Cannot delete member reports.")
    
    #All member reports deleted (default).
    elif flag == -1:
      print("All member reports deleted.")

    #No match found.
    elif flag == 0:
      print("No reports with the associated ID(s) found. Cannot delete member reports.")

    #Match found.
    else:
      print("Reports associated with the provided ID(s) deleted.")
    
    return flag
  

  ############################## Provider Reports Management ############################## 


  #Construct the fields required for a provider report and pass these fields into the report model.
  def makeProviderReport(self, providerId, date):

    # Required fields to assemble provider report:
    #   Provider ID
    #   Date
    #   Cost
    #--------------------
  
    #Get provider info.
    #provider = self.am.getAccountById(self.am, providerId)
    provider = self.am.accountManager.getAccountById(self.am, providerId)
    if provider == -1:
      print("No provider found with the supplied provider ID. Cannot generate provider report.")
      return -1

    #Get all member reports.
    #members = self.rm.getMemberReports(self.rm)
    members = self.rm.reportManager.getMemberReports(self.rm)
    if members == -1:
      print("No saved member reports. Cannot generate provider report.")
      return -1

    reports = []
    cost = 0

    #Collect member reports with relevant provider ID.
    for entry in members:
      if entry["provider id"] == providerId:
        reports.append(entry["report id"])
        cost += entry["cost"]
    
    #Check if any reports are found.
    if len(reports) == 0:
      print("No services by this provider saved in member reports. Cannot generate provider report.")
      return -1
    
    #return self.rm.makeProviderReport(self.rm, provider, reports, date, cost)
    return self.rm.reportManager.makeProviderReport(self.rm, provider, reports, date, cost)

  #Display provider reports associated with the passed member ID or report ID.
  #Display all if no arguments given.
  #Return fail if no match is found. Does not display report ID as it is arbitrary.
  def displayProviderReport(self, providerId=0, reportId=0):
  
    reports = []
    #reports = self.rm.getProviderReports(self.rm)
    reports = self.rm.reportManager.getProviderReports(self.rm)


    #Check for existing provider reports.
    if reports == -1:
      print("No provider reports saved. Cannot display provider reports.")
      return -1
    
    flag = 0
    #Display provider report depending on input.
    for entry in reports:
      if entry["provider id"] == providerId or entry["report id"] == reportId or (providerId == 0 and reportId == 0):

        print("\nService provider report generated on", entry["date"], "for:", entry["provider name"])
        print("Provider ID:", entry["provider id"])
        for service in entry["services"]:
          self.displayMemberReport(self, reportId=service)
        print("Total cost of services delivered by", entry["provider name"], ": $", entry["cost"])
        flag = 1

    if flag == 0:
      print("\nInvalid report and/or provider IDs supplied. Cannot generate provider report.")
      return 0
    
    return 1

  #Delete all provider reports associated with passed in provider ID, report ID, or all by default.
  def delProviderReports(self, providerId=0, reportId=0):

    #flag = self.rm.delProviderReports(self.rm, providerId, reportId)
    flag = self.rm.reportManager.delProviderReports(self.rm, providerId, reportId)

    #No provider reports exist.
    if flag == -2:
      print("No provider reports saved. Cannot delete provider reports.")
    
    #All provider reports deleted (default).
    elif flag == -1:
      print("All provider reports deleted.")
   
    #No match found.
    elif flag == 0:
      print("No reports with the associated ID(s) found. Cannot delete provider reports.")
    
    #Match found.
    else:
      print("Reports associated with the provided ID(s) deleted.")

    return flag


  ############################## Payable Reports Management ############################## 
    
#Construct the fields required for a payable report and pass these fields into the report model.
  def makePayableReport(self, date):
    # Required fields to assemble provider report:
    #   Date
    #   Report ID
    #   Cost
    #--------------------

    #provReports = self.rm.getProviderReports(self.rm)
    provReports = self.rm.reportManager.getProviderReports(self.rm)

    if provReports == -1:
      print("No provider reports saved. Cannot generate Accounts Payable report.")
      return -1

    repIds = [] 
    cost = 0
    for entry in provReports:
      repIds.append(entry["report id"])
      cost += entry["cost"]

    #return self.rm.makePayableReport(self.rm, date, repIds, cost)
    return self.rm.reportManager.makePayableReport(self.rm, date, repIds, cost)


  #Display payable reports associated with the passed report ID.
  #Display all if no arguments given.
  #Return fail if no match is found. 
  def displayPayableReport(self, reportId=0):

    #reports = self.rm.getPayableReports(self)
    reports = self.rm.reportManager.getPayableReports(self)

    #Payable report does not exist.
    if reports == -1:
      print("No payable reports saved.")
      return -1
    
    flag = 0

    #Display payable report if it exists depending on input provided.
    for entry in reports:
      if reportId == 0 or entry["report id"] == reportId:

        print("\t\n~ Accounts Payable report generated on", entry["date"], "~")
        print("\tAccounts Payable report ID:", entry["report id"])

        for id in entry["provider reports"]:
          self.displayProviderReport(self, reportId=id)
        
        print("\n\t~Total cost to be paid by ChocAn: $", entry["cost"], "~\n")

        flag = 1
    
    #Report ID does not exist.
    if flag == 0:
      print("\nNo accounts payable report found with the supplied report ID.")

    return flag

  #Delete all payable reports associated with passed in memberID or all by default.
  def delPayableReport(self, reportId=0):

    #flag = self.rm.delPayableReports(self.rm, reportId)
    flag = self.rm.reportManager.delPayableReports(self.rm, reportId)

    #No payable reports exist.
    if flag == -2:
      print("No accounts payable reports saved. Cannot delete accounts payable reports.")
   
    #All payable reports deleted (default).
    elif flag == -1:
      print("All accounts payable reports deleted.")
    
    #No match found.
    elif flag == 0:
      print("No reports with the associated ID(s) found. Cannot delete accounts payable reports.")
    #Match found.
    else:
      print("Reports associated with the provided ID(s) deleted.")

    return flag
