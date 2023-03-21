import random

def playRPSGame():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissor\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "The game is Tie!"

    if (user != 'r') and (user != 'p') and (user != 's'):
        print("Please enter valid option!")
        playRPSGame()

    #r>s, s>p, p>r
    if isWin(user,computer):
        return "You won!"

    return "You lost!"

def isWin(player, opponent):
    if (player == 'r' and opponent== 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(playRPSGame())



