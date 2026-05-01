#Simple Login script 
import getpass

username = input("Enter username: ")

if username == "admin":
    # This hides the characters
    password = getpass.getpass("Enter password: ")
    
    if password == "1234":
        print("WELCOME")
    else:
        print("Access Denied.")
else:
    print("User not found.")
  
  
  
