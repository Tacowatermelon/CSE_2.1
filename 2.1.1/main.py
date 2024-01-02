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