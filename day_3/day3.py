# ==========================================
# IntSyst - Day 3 of 100
# Python Loops
# Python Fundamentals to AI Engineering
# ==========================================

print("====================================")
print("             IntSyst")
print("       Python to AI Engineering")
print("           DAY 3: LOOPS")
print("====================================")


# ------------------------------------------
# PART 1: FOR LOOP
# ------------------------------------------

print("\n--- PART 1: FOR LOOP ---")

# A for loop repeats code for each item in a sequence.

for number in range(1, 6):
    print(number)


# ------------------------------------------
# PART 2: RANGE WITH STEP
# ------------------------------------------

print("\n--- PART 2: RANGE WITH STEP ---")

# range(start, stop, step)
# Generates even numbers from 2 to 10.

for number in range(2, 11, 2):
    print(number)


# ------------------------------------------
# PART 3: WHILE LOOP
# ------------------------------------------

print("\n--- PART 3: WHILE LOOP ---")

# A while loop repeats as long as the condition is True.

count = 1

while count <= 5:
    print(count)
    count += 1


# ------------------------------------------
# PART 4: BREAK STATEMENT
# ------------------------------------------

print("\n--- PART 4: BREAK STATEMENT ---")

# break immediately stops the loop.

for number in range(1, 11):

    if number == 6:
        break

    print(number)


# ------------------------------------------
# PART 5: CONTINUE STATEMENT
# ------------------------------------------

print("\n--- PART 5: CONTINUE STATEMENT ---")

# continue skips the current iteration.

for number in range(1, 6):

    if number == 3:
        continue

    print(number)


# ------------------------------------------
# PART 6: NESTED LOOPS
# ------------------------------------------

print("\n--- PART 6: NESTED LOOPS ---")

# A nested loop is a loop inside another loop.

for row in range(3):

    for column in range(3):
        print("*", end=" ")

    print()


# ------------------------------------------
# PART 7: MULTIPLICATION TABLE
# ------------------------------------------

print("\n--- PART 7: MULTIPLICATION TABLE ---")

# Generate the multiplication table of 5.

for number in range(1, 11):
    print(f"5 x {number} = {5 * number}")


# ------------------------------------------
# PART 8: NUMBER GUESSING GAME
# ------------------------------------------

print("\n--- PART 8: NUMBER GUESSING GAME ---")

import random

# Generate a random number between 1 and 100.
secret_number = random.randint(1, 100)

# Initialize game attempts.
attempts = 0
max_attempts = 7

print("\nWelcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print(f"You have {max_attempts} valid attempts to guess it.")

# Continue the game while attempts remain.
while attempts < max_attempts:

    try:
        guess = int(input("\nEnter your guess: "))

    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue

    # Validate the player's guess.
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    # Count only valid guesses.
    attempts += 1

    print(f"Attempt {attempts} of {max_attempts}")

    # Compare the guess with the secret number.
    if guess < secret_number:
        print("Too low! Try a higher number.")

    elif guess > secret_number:
        print("Too high! Try a lower number.")

    else:
        print("\nCongratulations! You guessed the correct number!")
        print(f"The secret number was {secret_number}.")
        break

else:
    # This runs when the loop finishes without break.
    print("\nGame Over! You used all your attempts.")
    print(f"The correct number was {secret_number}.")


# ------------------------------------------
# DAY 3 SUMMARY
# ------------------------------------------

print("\n====================================")
print("          DAY 3 COMPLETED!")
print("====================================")

print("Today, you learned:")
print("1. For Loops")
print("2. Range Function")
print("3. While Loops")
print("4. Break Statement")
print("5. Continue Statement")
print("6. Nested Loops")
print("7. Practical Loop Applications")
print("8. Number Guessing Game")

print("\nNext Lesson: Day 4 - Python Functions")
print("Keep Learning with IntSyst!")
print("====================================")