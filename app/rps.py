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
#quick alias to facilitate some copying and pasting
# we will soon move this into a function anyway
u = user_choice
c = computer_choice
if u == "rock" and c == "rock":
    print("TIE GAME")
elif u == "rock" and c == "paper":
    print("COMPUTER WINS")
elif u == "rock" and c == "scissors":
    print("USER WINS")
elif u == "paper" and c == "rock":
    print("COMPUTER WINS") # OOPS
elif u == "paper" and c == "paper":
    print("TIE GAME")
elif u == "paper" and c == "scissors":
    print("USER WINS") # OOPS
elif u == "scissors" and c == "rock":
    print("COMPUTER WINS")
elif u == "scissors" and c == "paper":
    print("USER WINS")
elif u == "scissors" and c == "scissors":
    print("TIE GAME")