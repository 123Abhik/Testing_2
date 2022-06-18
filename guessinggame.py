import random
highest=10
answer = random.randint(1,highest)
print("Please guess a number between 1 and {}:".format(highest))
guess=int(input())
if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done! you have guessed it correctly")
    else:
        print("Sorry! Wrong Guess. It is actually {}".format(answer))
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done! you have guessed it correctly")
    else:
        print("Sorry! Wrong Guess. It is actually {}".format(answer))
else:
    print("You got it the first time")

