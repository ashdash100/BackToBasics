# Day 4 - 4/3
import random

def numberGuesser():
  """Generate a random number from 1-100 for the user to guess. """
  mynum = random.randint(1,100)
  print("Hello! Welcome to my number guesser!")
  print("This is Day 2 of my Back To Basics Coding series\n")
  guess = int(input("I have selected a random number between 1 and 100. Please input a number and I will tell you if my number is higher or lower.\n"))
  analyzer(guess, mynum)
  
def anotherGuess():
  """ Allows the user to guess again after an incorrect guess.
  :rtype: int
  :return: guess
  """
  guess = int(input("\nPlease guess another number.\n"))
  return guess

def analyzer(guess, mynum):
  """ Checks if the user's guess is the same as the randomly generated number. If inputs are equal, program stops. If inputs are not equal, then anotherGuess() and analyzer() are called again 
  :param int guess: The user's guess
  :param int mynum: The randomly generated number
  """
  if guess == mynum:
    print("Congrats! You have guessed the correct number!")
  if guess < mynum:
    print("Good guess. My number is higher.")
    guess = anotherGuess()
    analyzer(guess, mynum)
  if guess > mynum:
    print("Good guess. My number is lower.")
    guess = anotherGuess()
    analyzer(guess, mynum)

numberGuesser()
