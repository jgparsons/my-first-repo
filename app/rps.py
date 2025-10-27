import random
VALID_OPTIONS = ["rock","paper","scissors"]
#ask user for input
user_choice = input("Please chhoose one of 'rock,' 'paper,' or 'scissors.'")
print("user choice:", user_choice)
#validations
if user_choice not in VALID_OPTIONS:
    print("Oops")
    exit()
#generate a random computer choice
computer_choice = random.choice(VALID_OPTIONS)
print("computer choice:", computer_choice)
#determine the winner
