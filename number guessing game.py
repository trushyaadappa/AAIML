import random

secret_number = random.randint(1, 5)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 5.")

while True:
    try:
        guess = int(input("Take a guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it: {secret_number}")
        break