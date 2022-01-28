import random

# Create riddle dictionary
riddle_dictionary = {
  "shadow": "Only one color, but not one size, Stuck at the bottom, yet easily flies. Present in sun, but not in rain, Doing no harm, and feeling no pain. What is it?",
  "120" : "Jenna wrote all the numbers from 300 to 400 on a piece of paper. How many times did she write the digit 3?",
  "mirror" : "If you drop me, I'm sure to crack. Give me a smile, and I'll always smile back. What am I?"
}

# Get random riddle

riddle_list = list(riddle_dictionary.values())
random_riddle = random.choice(riddle_list)

# Print Riddle and ask for Answer
print(random_riddle)
user_answer = input("Enter Answer: ")

# Check if answer is in dictionary
if user_answer in riddle_dictionary:
  print("Correct")
else:
  print("Try again")
