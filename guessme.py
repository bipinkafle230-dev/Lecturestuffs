import random


# initialize the random number between 1 to 100

number=random.randint(1,100)
print("I am thinking numbers inside 1 to 100:")


# Initialize the guess variable and the number of tries

guess = 0
tries = 0


# Keep looping
while guess != number:
    try:
        guess = int(input("Take a guess: "))
        tries += 1  # This is the same as tries = tries + 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {tries} tries!")
    except ValueError:
        print("Please enter a valid number!")

