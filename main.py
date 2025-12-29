import random

print(" Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Make a guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f" Correct! You guessed it in {attempts} attempts!, successfully")
        break

