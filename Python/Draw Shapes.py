import turtle

screen = turtle.getscreen()
tom = turtle.Turtle()

print("This program will draw a shape")

# Get my choice
choice = input("Enter [1] square [2] triangle [3] circle:  ")
choice = int(choice)

# Choice Select
if choice == 1: 
    for _ in range(4):
        tom.right(90)
        tom.forward(100)
elif choice == 2:
    for _ in range(3):
        tom.right(60)
        tom.forward(100)
        tom.right(60)
elif choice == 3:
    tom.circle(100)
else: 
    print("I do not understand... Please try again")

turtle.done()
