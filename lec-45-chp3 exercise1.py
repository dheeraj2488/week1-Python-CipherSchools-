winning_number=input("guess a number")
user_input=int(winning_number)
if user_input==winning_number:
    print("you win!!")
else:
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")        