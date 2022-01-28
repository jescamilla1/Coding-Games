import random

# Create random number
random_number = random.randint(0, 100)

# Ask user for number
user_guess = int(input("Enter your guess: 0-100 "))

# Compare numbers
while(True):
  if random_number == user_guess:
    print("Correect!!!!")
  else:
    print("Wrong answer try again...")
    user_guess = int(input("Try again 1-100: "))
