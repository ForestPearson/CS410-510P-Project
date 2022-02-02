# Authentication function. Takes in a login and password.
# See accounts.JSON for current login credentials

from login_handler import *

def auth():
    while True:
        auth = loginClass()
        print (65 * "-")
        print ("""Chocoan Provider Terminal System""")
        print (65 * "-" + "\n\n\n")

        username = input("Please provide username: ")
        password = input("Password: ")

        log = auth.login(username, password)

        #If username/password do not exist, JSON will return -1
        if log == -1:
            print("Invalid Login\n\n")
            choice = input("Try Again [Y/N]\n")
            
            #Break out of the while if user does not want to keep trying.
            if(choice.upper() == 'N'):
                break


auth()