import random
y = int(random.randrange(1,1001))
guess = int(input("Input a number between 1 and 1000"))
z = 1
while guess != y:
    if guess < y:
        print("Too Low")
    elif guess > y:
        print("Too High")
    z +=1
    guess = int(input())
if guess == y:
    print("Correct! The answer was: " + str(y))
    print("Number of guesses: " + str(z))