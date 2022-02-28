# Account Management allos for creation of new JSON objects in accounts.JSON
# Allows for New account creation, Updating account information, Deletion
# Search by ID and Username

import json

class accountManager:

    # Makes a new JSON account object and stores it in the "Database"
    def makeAccount(self, **fields):
        # Required fields for all accounts:
        #   Name
        #   ID
        #   Phone
        #   Address
        #   Username
        #   Password
        #   Type        (member, provider, admin)
        #-----------------
        # Additional fields for members:
        #   Status
        #   Services received
        #-----------------
        # Additional fields for service providers:
        #   Services delivered
        #   Services offered
        #-----------------

        data = []

        # Attempts to read in JSON from the database
        # this is so that we can append the new entry to the end of the JSON
        try:
            with open('accounts.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            pass

        # determine the ID to assign to the new user
        if data:
            id = (data[len(data) - 1]["id"] + 1)
        else:
            id = 1

        addFields = []
        
        # determine the type of the account
        if fields["type"] == "member":
            status = {"status: ": fields["status"]}
            services = {"services: ": []} # since this is a new account, there should be no services
            addFields.append(status)
            addFields.append(services)
        elif fields["type"] == "provider":
            services = {"services: " : []} # since this is a new account, there should be no services
            offered = {"offered: " : fields["offered"]}
            addFields.append(services)
            addFields.append(offered)
            
        newAccount = {
            "id":           id,
            "name":         fields["name"],
            "phone":        fields["phone"],
            "address":      fields["address"],
            "username":     fields["username"],
            "password":     fields["password"],
            "type":         fields["type"],
            "additional":   addFields
            }

        data.append(newAccount)
        with open('accounts.JSON', 'w') as outfile:
            json.dump(data, outfile, indent=1)

        return 1
            

    # Updates an existing account from the "Database"
    # will return an error if account to update does not exist
    def updateAccount(self, id, **fields):

        # attempt to read in accounts from the database
        try:
            with open('accounts.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            print("There are no accounts in the database!")
            return -1
        
        flag = 0

        # remove any account whose id matches the id we want to remove
        for entry in data:
            if entry["id"] == id:
                for field in fields:
                    entry[field] = fields[field]
                flag = 1
        
        # if no account was updated 
        if flag == 0:
            return -1
        
        with open('accounts.JSON', 'w') as outfile:
            json.dump(data, outfile, indent=1)
        
        return 1

    # Removes an existing account from the "Database"
    # will return an error if account to delete does not exist
    def delAccount(self, id):
        
        # attempt to read in accounts from the database
        try:
            with open('accounts.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            print("There are no accounts in the database!")
            return -1

        flag = 0

        # remove any account whose id matches the id we want to remove
        for entry in data:
            if entry['id'] == id:
                data.remove(entry)
                flag = 1

        # if no account was updated 
        if flag == 0:
            return -1
        
        with open('accounts.JSON', 'w') as outfile:
            json.dump(data, outfile, indent=1)
        
        return 1

    # Search account by ID Number
    def getAccountById(self, id):

        # attempt to read in accounts from the database
        try:
            with open('accounts.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            print("There are no accounts in the database!")
            return -1

        # retrieve account whose id matches the id passed in
        for entry in data:
            if entry["id"] == id:
                return entry
        
        return -1

    def getAccountByUsername(self, username):
        # attempt to read in accounts from the database
        try:
            with open('accounts.JSON', 'r') as readfile:
                data = json.load(readfile)
        except:
            print("There are no accounts in the database!")
            return -1

        #This checks each JSON entry as a list.
        for entry in data:
            #Converts JSON entry to lowercase, Converts Username input to lowercase.
            if entry["username"].lower() == username.lower():
                return entry
        
        return -1

    #example function calls

    #makeAccount(name="Bob", phone="555-555-5555", address="123 Sesame St.", username="Bobs", password="passw0rd", type="member", status="active")
    #makeAccount(name="Bobbie", phone="555-555-5555", address="123 Sesame St.", username="Bobbies", password="passw0rd", type="provider", offered=[1,2,3,4])
    #makeAccount(name="Hank", phone="555-555-5555", address="123 Sesame St.", username="Hanks", password="passw0rd", type="admin")
    #updateAccount(1, name="Steve", phone="555-555-5554")
    #getAccountById(2)
    #getAccountByUsername("Bobs")
    #delAccount(2)