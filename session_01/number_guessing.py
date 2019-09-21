# Import random module to generate random integers
import random

# Random integer between 1 and 100
target = random.randint(1, 100)

# Is the game still running?
running = True

print("I'm thinking of a number between 1 and 100.")

while running:  # This is shorthand for 'running == True'
  # Input player's guess as an integer
  guess = int(input("Take a guess: "))

  # Check player's guess against target number
  if guess < target:
    print("Too low!")
  elif guess > target:
    print("Too high!")
  else:
    print("You got it!")
    running = False  # Game is no longer running