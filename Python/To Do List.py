import os
import time
from colorama import Fore, Style

todolist = []

#ask how many things to do today
num = int(input("How many things are we doing today? "))

# populate list
for x in range(num):
  temp = input("Enter to-do {0}: ".format(x+1))
  todolist.append(temp)
# Clear console
os.system('clear')

#run while you still have chores
chores = True
while chores:
  if len(todolist):
    x = 1
    for todo in todolist:
      print("{0}. {1}".format(str(x), todo))
      x += 1
    
    #ask if anything has been completed
    temp = input("Did you complete anything? y or n ")
    if temp == "y":
      temp = int(input("Which item? enter number: "))
      del todolist[temp-1]
      os.system('clear')
    else: 
      print(Fore.RED + "Great, go get things done")
      print(Style.RESET_ALL)
      time.sleep(2)
      os.system('clear')
  else:
    # No more items in list
    print(Fore.GREEN + "Nice work! Restart the program if you want to create another list")
    print(Style.RESET_ALL)
    chores = False

