import random

secret = random.randint(1, 100)

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Correct! You win 🎉")
        break
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")
