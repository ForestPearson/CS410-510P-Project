import json

class reportManager:

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

        # Attempts to read in JSON from the database
        # this is so that we can append the new entry to the end of the JSON
        try:
            with open('memberReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            pass

        # Assign a report id
        if data:
            id = (data[len(data)-1]["report id"] + 1)
        else:
            id = 1

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

        data.append(newReport)

        with open('memberReports.JSON', 'w') as outfile:
            json.dump(data, outfile, indent=1)

        return 1


    # Only allows one report saved per provider at any time. Most recent added report
    # from a given provider is the one that's saved.
    def makeProviderReport(self, provider, reports, date, cost):
        
        # Required fields for member report:
        #   Provider Name
        #   Provider ID
        #   Services performed (list of member report IDs)
        #   Date
        #-----------------------

        data = []

        # Attempts to read in JSON from the database
        # this is so that we can append the new entry to the end of the JSON
        try:
            with open('providerReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            pass
        
        if data: 
            id = (data[len(data)-1]["report id"] + 1)
        else:
            id = 1

        newReport = {
            "provider name"     :   provider["name"],
            "provider id"       :   provider["id"],
            "services"          :   reports,
            "date"              :   date,
            "cost"              :   cost,
            "report id"         :   id
        }

        # Check for previous provider report from the same provider
        for entry in data:

            if entry["provider id"] == newReport["provider id"]:

                # Remove previous report                    
                self.delProviderReports(self, reportId=entry["report id"])
                data = self.getProviderReports(self)

                # Check for empty file
                if data == -1:
                    data = []
                break
        
        data.append(newReport)
        
        with open('providerReports.JSON', 'w') as outfile:
            json.dump(data, outfile, indent=1)
        return 1
    

    def makePayableReport(self, date, repIds, cost):
        
        # Required fields for payable report:
        #   Date
        #   Report ID
        #   Services performed (list of all service provider report IDs)
        #   Total cost
        #-----------------------

        data = []

        # Attempts to read in JSON from the database
        # this is so that we can append the new entry to the end of the JSON
        try:
            with open('payableReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            pass
        
        if data:
            id = data[len(data)-1]["report id"] + 1
        else:
            id = 1

        newReport = {
            "date"              :   date,
            "report id"         :   id,
            "provider reports"  :   repIds,
            "cost"              :   cost
        }

        data.append(newReport)
        
        with open('payableReports.JSON', 'w') as outfile:
            json.dump(data, outfile, indent=1)
        return 1


    # Add service passed in from controller
    def addService(self, serviceName, cost):
        
        # Required fields for service:
        #   ID
        #   Name
        #   Cost
        #-----------------------

        data = []

        # Attempts to read in JSON from the database
        # this is so that we can append the new entry to the end of the JSON
        try:
            with open('services.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            pass

        # Assign id
        if data:
            id = data[len(data)-1]["id"] + 1
        else:
            id = 1

        newService = {
            "name"      :   serviceName,
            "id"        :   id,
            "cost"      :   cost
        }

        data.append(newService)
        
        with open('services.JSON', 'w') as outfile:
            json.dump(data, outfile, indent=1)
        return 1


    # Pull services from database
    # Pulls all services if no service code is provided
    def getService(self, serviceCode=0):
        data = []
    
        try:
            with open('services.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -1

        if serviceCode == 0:
            return data
        
        for entry in data:
            if entry["id"] == serviceCode:
                return entry

        return 0
    

    # Delete services indicated by service code
    # 4 possible return states: 
    # -2 if no services saved, -1 if all services deleted (default)
    #  0 if no match found with serviceCode, 1 if match found 
    def delService(self, serviceCode=0):

        data = []

        try:
            with open('services.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -2

        # Default service code of -1 indicates delete all
        if serviceCode == 0:
            open('services.JSON', 'w').close()
            return -1

        new = []
        flag = 0 

        # Copy all elements into new object, excluding deleted ones
        for entry in data:
            if entry["id"] == serviceCode:
                flag = 1
            else:
                new.append(entry)
        
        # Write new object to file
        if len(new) > 0:
            with open('services.JSON', 'w') as outfile:
                json.dump(data, outfile, indent=1)
                
        # Prevents writing an empty array into the file
        else:
            open('services.JSON', 'w').close()

        return flag
    
    
    # Pull member reports from database and return as json object
    def getMemberReports(self):

        data = []

        try:
            with open('memberReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -1

        return data


    # Delete all member reports associated with passed in memberID or reportId.
    # Delete all reports by default
    def delMemberReports(self, memberId=0, reportId=0):

        data = []

        try: 
            with open('memberReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -2
        
        # Default option, delete all reports 
        if memberId == 0 and reportId == 0:
            open('memberReports.JSON', 'w').close()
            return -1
        
        new = []
        flag = 0

        # Copy all elements into new object, excluding deleted ones
        for entry in data:
            if entry["member id"] == memberId and entry["report id"] == reportId:
                flag = 1
            else:
                 new.append(entry)
        
        # Write new data back to file
        if len(new) > 0:
            with open('memberReports.JSON', 'w') as outfile:
                json.dump(new, outfile, indent=1)

        # Prevent writing an empty array into the file
        else:
            open('memberReports.JSON', 'w').close()

        return flag


    # Pull provider reports from database and return as json object
    def getProviderReports(self):

        data = []

        try:
            with open('providerReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -1

        return data
    

    def delProviderReports(self, providerId=0, reportId=0):

        data = []

        try:
            with open('providerReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -2
        
        if providerId == 0 and reportId == 0:
            open('providerReports.JSON', 'w').close()
            return -1
        
        new = []
        flag = 0

        for entry in data:
            if entry["provider id"] == providerId or entry["report id"] == reportId:
                flag = 1
            else:
                new.append(entry)

        if len(new) > 0:
            with open('providerReports.JSON', 'w') as outfile:
                json.dump(new, outfile, indent=1)
        else:
            open('providerReports.JSON', 'w').close()

        return flag


    def getPayableReports(self):

        data = []

        try:
            with open('payableReports.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            return -1

        return data


    def delPayableReports(self, reportId=0):

        data = []

        try:
            with open('payableReports.JSON') as readfile:
                data = json.load(readfile)
        except:
            return -2

        if reportId == 0:
            open('payableReports.JSON', 'w').close()
            return -1
        
        new = []
        flag = 0

        for entry in data:
            if entry["report id"] == reportId:
                flag = 1
            else:
                new.append(entry)
        
        if len(new) > 0:
            with open('payableReports.JSON', 'w') as outfile:
                json.dump(new, outfile, indent=1)
        else:
            open('payableReports.JSON', 'w').close()

        return flag
            
