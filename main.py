import random
import art

print(art.logo)
computer_choice = random.randint(1,101)

print(computer_choice)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard':")


if level == 'easy':
  chances = 10
  while chances != 0:
    print(f"You have {chances} attempts remaining to guess the number. ")
    users_choice = int(input("Guess a number: "))
    if users_choice == computer_choice:
      print(f"You got it! The answer was {computer_choice}")
      chances = 0
      break
    elif users_choice > computer_choice:
      print("Too high")
    elif users_choice < computer_choice:
      print("Too low")
    chances -= 1 
    if chances == 0:
      print("Game over. You went out of moves")
elif level == 'hard':
  chances = 5
  while chances != 0:
    print(f"You have {chances} attempts remaining to guess the number.")
    users_choice = int(input("Guess a number: "))
    if users_choice == computer_choice:
      print(f"You got it! The answer was {computer_choice}")
      chances = 0
      break
    elif users_choice > computer_choice:
      print("Too high")
    elif users_choice < computer_choice:
      print("Too low")
    chances -= 1
    if chances == 0:
      print("Game over. You went out of moves")

else:
  print("invalid input")