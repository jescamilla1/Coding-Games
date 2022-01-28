from random import randint
from time import sleep
from colorama import Fore, Style

#correct order to compare against
correct = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Bots  random list of starter numbers
botAnswer = [randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10),randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)] 

learned = False
# loops until bot learns correct order
tries = 1
while learned == False:
  print(botAnswer)
  sleep(0.5)		
  for i in range(len(correct)): # assuming both bot and answer list are same length
    # Check values if wrong, bot guesses again
  	if correct[i] != botAnswer[i]:
		  botAnswer[i] = randint(1,10)
  tries = tries + 1
  if correct == botAnswer:
    print(Fore.GREEN +str(botAnswer))
    print(Style.RESET_ALL)
    print("I DID IT! it only took me " + str(tries) + " tries!")
    learned = True
  
