from random import randint
from art import logo
from replit import clear

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Check the user's guess against the actual answer.
def check_answer(guess, answer, turns):
  """checks answer against the guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You guessed correctly! The answer was {answer}.")

#Set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def game():
  print(logo)
  #Choose a number between 1 and 100

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)

  turns = set_difficulty()

  #Repeat until they get it wrong
  guess = 0
  while guess != answer:
    print(f"You have {turns} guesses remaining.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print(f"You've run out of guesses, you lose. The correct answer was {answer}.")
      return
    elif guess != answer:
      print("Guess again.")

while input ("Are you ready to play? Type 'yes' or 'no': ") == "yes":
  clear()
  game()



