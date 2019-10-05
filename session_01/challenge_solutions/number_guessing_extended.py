# Import random module to generate random integers
import random

# Random integer between 1 and 100
target = random.randint(1, 100)

# Count number of guesses
count = 0

# Limit for number of guesses
limit = 7

print("I'm thinking of a number between 1 and 100.")

while count <= limit:  # This is shorthand for 'running == True'
  # Input player's guess as an integer
  guess = int(input("Take a guess: "))
  count += 1

  # Check player's guess against target number
  if guess < target:
    print("Too low!")
  elif guess > target:
    print("Too high!")
  else:
    # Break from the loop – an alternative to this is to still use a 'running' bool
    break

if guess == target:
  print("You got it!")
  print(f"You took {count} guesses.")
else:
  print(f"Sorry, you ran out of guesses! The answer was {target}.")