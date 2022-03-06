from report_generation_handler import *
from datetime import date
import json

class providerHandler:
    def displayService(self):
        reportH = reportHandler()
        reportH.displayServices()
    def makeReport(self, provId):
        reportH = reportHandler()
        today = date.today()
        memberId = int(input("Enter member ID: "))
        if(providerHandler.validate(self, memberId) == 1):
            servId = int(input("Enter service ID: "))
            d1 = today.strftime("%m/%d/%y")
            reportH.makeMemberReport(memberId, provId, servId, d1)
    def requestReport(self):
        reportH = reportHandler()
        memberId = int(input("Enter member ID: "))
        reportH.displayMemberReport(memberId)
    def deleteMemberReport(self):
        reportH = reportHandler()
        memberId = int(input("Enter the member ID: "))
        reportId = int(input("Enter the report ID: "))
        reportH.delMemberReports(memberId = memberId, reportId = reportId)

    
    
    
    
    def validate(self, id):
        try:
            with open('records/accounts.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            pass
        for entry in data:
            if entry['id'] == id:
                print("id found")
                if entry['additional'][0]['status: '] == "active":
                    return 1
                else:
                    print("This member is not active")
                    return 0
        print("invalid ID")
        return 0
