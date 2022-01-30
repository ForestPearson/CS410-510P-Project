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
        if log == -1:
            print("Invalid Login")
        

auth()