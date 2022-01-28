import getpass
import os
import time

#user db
database = {"coolguy123@gmail.com": "123456", "supercat21@yahoo.com":"qwerty", "dogsnake@bing.com": "dogsarecool"}

found = False
while(not found):
  username = input("Enter Username: ")
  password = getpass.getpass("Enter Password: ")
  if username in database:
    while password != database[username]:
      password = getpass.getpass("Password Incorrect! Try again: ")
    os.system('clear')
    print("Welcome to the Club!")
    found = True
  else:
    print("They dont exist!")
    time.sleep(2)
    os.system('clear')
