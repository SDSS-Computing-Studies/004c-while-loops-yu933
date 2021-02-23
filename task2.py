#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
username = ""
password = ""

while username != "admin" and password != "12345":
    username=input("please enter username")
    password=input("please enter password")
    if username != "admin" and password != "12345":
        print("Access denied")
print("Access granted")