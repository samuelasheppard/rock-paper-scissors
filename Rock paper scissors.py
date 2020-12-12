import random

# Responses
LOSER = "Ha! You lose!"
WINNER = "Can you read my mind? You win!"
DRAW = "Great minds think a like!"

# Random choice number and word conversion functions
def computer_conversion(num):
    text = ["Rock!", "Paper!", "Scissors!"]
    print(text[num - 1])

def user_conversion(word):
    if word.lower() in ['rock', 'r']:
        return 1
    elif word.lower() in ['paper', 'p']:
        return 2
    elif word.lower() in ['scissors', 's']:
        return 3

def win(computerChoice, userResult):
    if computerChoice == userResult:
        return DRAW
    elif computerChoice == 1:
        return WINNER if userResult == 2 else LOSER
    elif computerChoice == 2:
        return WINNER if userResult == 3 else LOSER
    elif computerChoice == 3:
        return WINNER if userResult == 1 else LOSER

# Game loop
def gameLoop():
    # Initial start up
    name = input("Hello, what's your name? ")
    game = input("Hello {}, would you like to play rock, paper, scissors? ".format(name))
    while game != "No":
        userChoice = input("Rock, paper... scissors! ")
        userResult = user_conversion(userChoice)

        computerChoice = random.randint(1,3)
        computer_conversion(computerChoice)

        winner = win(computerChoice, userResult)
        print(winner)

        if winner == WINNER:
            game = input("Well done, {}. Would you like to play again? ".format(name))

    else:
        print("Thanks for playing {}".format(name))

gameLoop()