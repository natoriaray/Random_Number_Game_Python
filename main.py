import random

def check_num(user, ran):
  if ran == user:
    print("You guessed the correct number!")
  elif ran > user:
    user_num = int(input("Your number is less than the secret number. Type in a new number: "))
    check_num(user_num, ran_num)
  elif ran < user:
    user_num = int(input("Your number is greater than the secret number. Type in a new number: "))
    check_num(user_num, ran_num)
  else:
    print("There was an error in your input")

start_game = input("Would you like to play this game? y or n: ").lower()

if start_game == "y":
  while True:
    ran_num = random.randint(1, 20)
    user_num = int(input("Type in a number between 1 and 20: "))
    check_num(user_num, ran_num)
    play_again = input("Would you like to play again? y or n").lower()
    if play_again == "n":
      print("See you again next time!")
      break
elif start_game == "n":
  print("See you again next time!")
else:
  print("There was an error with you input")
