import random

maxrange= input("Enter range for number: ")
if maxrange.isdigit():
    maxrange = int(maxrange) 
    if maxrange <= 0:
        print("Try to enter a number greater than 0 next time!")

else:
    print("Try to enter a number next time!")
    quit()

random_number = random.randint(0,maxrange)

count=0

while True:
    count += 1
    guess = input("Try your luck : \n")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Enter a number!! ")
        continue

    if guess == random_number:
        print("You got it right!")
        break
    elif guess < random_number:
        print("Guess a little higher")
    else:
        print("Guess a little lower! ")

print("You got it in", count, "guesses !")