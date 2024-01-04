count=1
while count <=3:
    print("Hello World")
    count = count + 1

def count_down():
    global number
    for number in range (11):
        print (number)
    return "Blast off!"
print(count_down())

name = input("What is your name?")
print(name)

import random

number = random.randint (1,10)
guess = input("Guess an integer between 1 and 10 ")
guess = int(guess)
if number == guess:
    print("Correct!")
else:
    print("Incorrect. " + "The number was " + str(number))


import math

radius = float(input("What is the radius of the tire?"))
seconds = float(input("What is the time in seconds it traveled for?"))

circumference = (2 * 3.14) * radius
minutes = seconds / 60
remainder = seconds % 60
print("It traveled ", int(minutes), "minutes and ", remainder, " seconds.")
print("The tire circumference is " + str(circumference))


