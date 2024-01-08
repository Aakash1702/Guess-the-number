import random
easy_mode = 10
hard_mode = 5

def set_difficulty():
  diff_mode = input("pick difficulty level easy to hard: ")
  if diff_mode == "easy":
    return easy_mode
  elif diff_mode == "hard":
    return hard_mode

def checker(guess, number, turns):
  if guess>number:
    print("Too high")
    return turns - 1
  elif guess<number:
    print("Too low")
    return turns - 1
  else:
    print(f"You guessed it right {number}")

  
def guess():
  print("Welcome to Game guess the number")
  print("I am thinking of a number between 1 and 100")
  number = random.randint(1,100)
  print(f"number = {number}")
  turns = set_difficulty()
  guess = 0
  while guess != number:
    print(f"You have {turns} left")
    guess = int(input("make a guess: "))
    turns =checker(guess, number, turns)
    if turns == 0:
      print("You are out of guesses You lose")
      return



guess()
