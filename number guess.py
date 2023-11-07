import random


secret_number = random.randint(1, 1000)

print("Welcome to the Number Guessing Game Made By Sakshi!")
print("I am thinking of a number between 1 and 1000.")


attempts = 1

while True:
    try:
       
        guess = int(input("Please guess the number: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Try again. Your guess is too low.")
        else:
            print("Try again. Your guess is too high.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
