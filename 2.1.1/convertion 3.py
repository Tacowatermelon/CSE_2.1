my_num=15
secret_num=25

def num_eval():
    if my_num > secret_num:
        print ("Your number was too large.")
    elif my_num < secret_num:
        print ("Your number was too small.")
    else:
        print ("Your number is equal.")

while (my_num != secret_num):
    my_num = int(input("Guess a number between 1 and 100 inclosive."))
    num_eval()


