import random

top_of_range=input("Enter the number:")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range <=0:
        print("enter the number above 0")
        quit()

else:
    print("enter a number")
    quit()

random_number=random.randint(0,top_of_range)
guesses=0

while True:
    guesses+=1
    if guesses==5:
        print("You are almost reached the maximum guesses.")
        quit()
    user_guess=input("enter the gussing number:")
    if user_guess.isdigit():
        user_guess=int(user_guess)

        if user_guess <0:
            print("entr the number above or equal to  0")
            continue
    else:
        print("type a number next time")
        continue

    if user_guess == random_number:
        print("Great job you win!")
        break
    elif user_guess > random_number:
        print("Try a number below ")

    else:
        print("Try a number above ")








