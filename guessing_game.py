import random

secret_number = random.randint(1, 10)
attempts = 3

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10.")
print("You have 3 attempts.")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed correctly!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    attempts = attempts - 1

    if attempts > 0:
        print("Attempts remaining:", attempts)

if attempts == 0 and guess != secret_number:
    print("Game over! The number was", secret_number)
