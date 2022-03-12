import json

class reportManager:

    # Create member report with passed in data from controller.
    def makeMemberReport(self, member, provider, service, date):

        # Required fields for member report:
        #   Member name
        #   Member ID
        #   Provider name
        #   Provider ID
        #   Service name
        #   Service ID
        #   Service cost
        #   Date
        #-----------------------

        data = []

        # Attempts to read in JSON from the database so that we can append the new entry to the end of the JSON.
        try:
            with open('records/memberReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            pass

        # Assign ID to this report.
        if data:
            id = (data[len(data)-1]["report id"] + 1)
        else:
            id = 1

        # Creates a new report with specific arguments passed in from report_generation_handler.py.
        # Pulls data from proper database based on the variable types.
        newReport = {
            "member name"    :   member["name"],
            "member id"      :   member["id"],
            "provider name"  :   provider["name"],
            "provider id"    :   provider["id"],
            "service"        :   service["name"],
            "service code"   :   service["id"],
            "cost"           :   service["cost"],
            "date"           :   date,
            "report id"      :   id 
        }

        # Add the new report into the database of memberReports.JSON.
        data.append(newReport)
        # Method dump() will convert Python objects into JSON objects.
        with open('records/memberReports.JSON', 'w') as outfile:
            json.dump(data, outfile, indent=1)

        return 1


    # Create provider report with passed in data from controller.
    # Only allows one report saved per provider at any time.
    # Most recent added report from a given provider is the one that's saved.
    def makeProviderReport(self, provider, reports, date, cost):
        
        # Required fields for member report:
        #   Provider Name
        #   Provider ID
        #   Services performed (list of member report IDs)
        #   Date
        #-----------------------

        data = []

        # Attempts to read in JSON from the database so that we can append the new entry to the end of the JSON.
        try:
            with open('records/providerReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            pass
        
        # Assign ID to this report.
        if data: 
            id = (data[len(data)-1]["report id"] + 1)
        else:
            id = 1

        # Creates a new report with specific arguments passed in from report_generation_handler.py.
        # Pulls data from proper database based on the variable types.
        newReport = {
            "provider name"     :   provider["name"],
            "provider id"       :   provider["id"],
            "services"          :   reports,
            "date"              :   date,
            "cost"              :   cost,
            "report id"         :   id
        }

        # Check for previous provider report from the same provider.
        for entry in data:

            if entry["provider id"] == newReport["provider id"]:

                # Remove previous report.                 
                self.delProviderReports(self, reportId=entry["report id"])
                data = self.getProviderReports(self)

                # Check for empty file.
                if data == -1:
                    data = []
                break

        # Add the new report into the database of providerReports.JSON.
        data.append(newReport)
        
        with open('records/providerReports.JSON', 'w') as outfile:
            json.dump(data, outfile, indent=1)
        return 1
    
    # Create payable report with passed in data from controller.
    def makePayableReport(self, date, repIds, cost):
        
        # Required fields for payable report:
        #   Date
        #   Report ID
        #   Services performed (list of all service provider report IDs)
        #   Total cost
        #-----------------------

        data = []

        # Attempts to read in JSON from the database so that we can append the new entry to the end of the JSON.
        try:
            with open('records/payableReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            pass

        # Assign ID to this report.  
        if data:
            id = data[len(data)-1]["report id"] + 1
        else:
            id = 1

        # Creates a new report with specific arguments passed in from report_generation_handler.py.
        # Pulls data from proper database based on the variable types.
        newReport = {
            "date"              :   date,
            "report id"         :   id,
            "provider reports"  :   repIds,
            "cost"              :   cost
        }

        # Add the new report into the database of payableReports.JSON.
        data.append(newReport)
        
        with open('records/payableReports.JSON', 'w') as outfile:
            json.dump(data, outfile, indent=1)
        return 1


    # Add service passed in from controller.
    def addService(self, serviceName, cost):
        
        # Required fields for service:
        #   ID
        #   Name
        #   Cost
        #-----------------------

        data = []

        # Attempts to read in JSON from the database so that we can append the new entry to the end of the JSON.
        try:
            with open('records/services.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            pass

        # Assign ID to this report.
        if data:
            id = data[len(data)-1]["id"] + 1
        else:
            id = 1

        # Creates a new report with specific arguments passed in from report_generation_handler.py.
        # Pulls data from proper database based on the variable types.
        newService = {
            "name"      :   serviceName,
            "id"        :   id,
            "cost"      :   cost
        }


        # Add the new report into the database of services.JSON.
        data.append(newService)
        
        with open('records/services.JSON', 'w') as outfile:
            json.dump(data, outfile, indent=1)
        return 1


    # Pull services from services.JSON database.
    def getService(self, serviceCode=0):
        data = []
    
        try:
            with open('records/services.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -1

        # Pulls all services if no service code is provided.
        if serviceCode == 0:
            return data
        
        # Pulls specific service provided service code.
        for entry in data:
            if entry["id"] == serviceCode:
                return entry

        return 0
    

    # Delete services indicated by service code.
    # Four possible return states:
    # Found match: 1
    # No found match: 0
    # All services deleted: -1
    # No saved services: -2
    def delService(self, serviceCode=0):

        data = []

        # Return -2 if no services exist.
        try:
            with open('records/services.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -2

        # Return -1 for all services being deleted.
        if serviceCode == 0:
            open('records/services.JSON', 'w').close()
            return -1

        new = []
        flag = 0 

        # Copy all elements into new object, excluding deleted ones.
        # flag = 1 return found match with the provided service code.
        for entry in data:
            if entry["id"] == serviceCode:
                flag = 1
            else:
                new.append(entry)
        
        # Write updated data to file.
        if len(new) > 0:
            with open('records/services.JSON', 'w') as outfile:
                json.dump(data, outfile, indent=1)
                
        # Prevents writing an empty array into the file.
        else:
            open('records/services.JSON', 'w').close()

        return flag
    
    
    # Pull member reports from database and return as json object.
    def getMemberReports(self):

        data = []
        try:
            with open('records/memberReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -1

        return data


    # Delete member reports associated with the passed in member ID or report ID.
    # Delete all reports by default.
    # Four possible return states:
    # Found match: 1
    # No found match: 0
    # All member reports deleted: -1
    # No saved member reports: -2
    def delMemberReports(self, memberId=0, reportId=0):

        data = []

        # Return -2 if no member reports exist.
        try: 
            with open('records/memberReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -2
        
        # Return -1 for deleting all member reports.
        if memberId == 0 and reportId == 0:
            open('records/memberReports.JSON', 'w').close()
            return -1
        
        new = []
        flag = 0

        # Copy all elements into new object, excluding deleted ones.
        for entry in data:
            if entry["member id"] == memberId and entry["report id"] == reportId:
                flag = 1
            else:
                 new.append(entry)
        
        # Write updated data back to file.
        if len(new) > 0:
            with open('records/memberReports.JSON', 'w') as outfile:
                json.dump(new, outfile, indent=1)

        # Prevent writing an empty array into the file.
        else:
            open('records/memberReports.JSON', 'w').close()

        return flag


    # Pull provider reports from database and return as json object.
    def getProviderReports(self):

        data = []
        try:
            with open('records/providerReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -1

        return data
    

    # Delete provider reports associated with the passed in provider ID or report ID.
    # Delete all reports by default.
    # Four possible return states:
    # Found match: 1
    # No found match: 0
    # All provider reports deleted: -1
    # No saved provider reports: -2
    def delProviderReports(self, reportId=0):

        data = []

        # Return -2 if no provider reports exist.
        try:
            with open('records/providerReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -2

        # Return -1 for deleting all provider reports.  
        if reportId == 0:
            open('records/providerReports.JSON', 'w').close()
            return -1
        
        new = []
        flag = 0

        # Copy all elements into new object, excluding deleted ones.
        for entry in data:
            if entry["report id"] == reportId:
                flag = 1
            else:
                new.append(entry)

        # Write updated data back to file.
        if len(new) > 0:
            with open('records/providerReports.JSON', 'w') as outfile:
                json.dump(new, outfile, indent=1)
        
        # Prevent writing an empty array into the file.
        else:
            open('records/providerReports.JSON', 'w').close()

        return flag


    # Pull payable reports from database and return as json object.
    def getPayableReports(self):

        data = []
        try:
            with open('records/payableReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -1

        return data


    # Delete provider reports associated with the passed in report ID.
    # Delete all reports by default.
    # Four possible return states:
    # Found match: 1
    # No found match: 0
    # All member reports deleted: -1
    # No saved member reports: -2
    def delPayableReports(self, reportId=0):

        data = []

        # Return -2 if no payable reports exist.
        try:
            with open('records/payableReports.JSON') as readfile:
                data = json.load(readfile)
        except:
            return -2

        # Return -1 for deleting all payable reports.  
        if reportId == 0:
            open('records/payableReports.JSON', 'w').close()
            return -1
        
        new = []
        flag = 0

        # Copy all elements into new object, excluding deleted ones.
        for entry in data:
            if entry["report id"] == reportId:
                flag = 1
            else:
                new.append(entry)
        
        # Write updated data back to file.
        if len(new) > 0:
            with open('records/payableReports.JSON', 'w') as outfile:
                json.dump(new, outfile, indent=1)
                
        # Prevent writing an empty array into the file.
        else:
            open('records/payableReports.JSON', 'w').close()

        return flag
            
