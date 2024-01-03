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

number = random.randint(1, 10)
guess = input("Guess an integer betweer 1 and 10 ")
guess = int(guess)
if number == guess:
    print("Correct!")
else:
    print("Incorrect. " + "The number was " + str(number))


