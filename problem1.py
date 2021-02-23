##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""
import time
username = ""
password =""
guess = 0
while username != "admin" or password != "12345" :
    username=input("please enter username").strip()
    password=input("please enter password").strip()
    if username != "admin" or password != "12345":
        print("Access denied")
        guess=guess+1
        time.sleep(0.1)
        if guess > 3:
            break
    else:
        print("Access granted")