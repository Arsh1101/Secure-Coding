import sys

username = input("Enter your username: ")
password = input("Enter your password: ")


def wrongCode():
    #The user can input different inputs (Even emojy)
    #We have to find a standard way to show it on out put.
    if username == "admin" and password == "password":
        sys.stdout.write("Welcome, admin!")
    else:
        sys.stdout.write("Invalid username or password -> " + username + " - " + password + " .")


def  correctCode():
    # 'utf-8' is a standard way to show the results to user.
    if username == "admin" and password == "password":
        sys.stdout.write("Welcome, admin!".encode('utf-8'))
    else:
        sys.stdout.write("Invalid username or password -> " + username.encode('utf-8') + " - " + password.encode('utf-8') + " .")


wrongCode()
