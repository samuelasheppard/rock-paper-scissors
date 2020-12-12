import random

# Possible answers
ROCK = ["ROCK", "Rock", "rock", "R", "r"]
PAPER = ["PAPER", "Paper", "paper", "P", "p"]
SCISSORS = ["SCISSORS", "Scissors", "scissors", "S", "s"]

# Responses
LOSER = "Ha! You lose!"
WINNER = "Can you read my mind? You win!"
DRAW = "Great minds think a like!"

# Random choice number and word conversion functions
def computer_conversion(num):
    if num == 1:
        result = ("Rock!")
        print(result)
    if num == 2:
        result = ("Paper!")
        print(result)
    if num == 3:
        result = ("Scissors!")
        print("Scissors!")

def user_conversion(word):
    if word in ROCK:
        return 1
    if word in PAPER:
        return 2
    if word in SCISSORS:
        return 3

def win():
    if computerChoice == userResult:
        print(DRAW)
    if computerChoice == 1 and userResult == 3:
        print(LOSER)
    if computerChoice == 3 and userResult == 2:
        print(LOSER)
    if computerChoice == 2 and userResult == 1:
        print(LOSER)
    if computerChoice == 3 and userResult == 1:
        print(WINNER)
        return "WINNER"
    if computerChoice == 2 and userResult == 3:
        print(WINNER)
        return "WINNER"
    if computerChoice == 1 and userResult == 2:
        print(WINNER)
        return "WINNER"

# Initial start up
name = input("Hello, what's your name? ")
game = input("Hello {}, would you like to play rock, paper, scissors? ".format(name))

# Game loop
while game != "No":
    userChoice = input("Rock, paper... scissors! ")
    userResult = user_conversion(userChoice)

    computerChoice = random.randint(1,3)
    computerResult = computer_conversion(computerChoice)
    winner = win()
    if winner == "WINNER":
        game = input("Well done, {}. Would you like to play again? ".format(name))

else:
    print("Thanks for playing {}".format(name))
