import random
from colorama import Fore, Back, Style

def game():
    player_move = input(Fore.YELLOW+"Choose [R]ock, [P]aper or [S]cissors: ")

    if player_move.lower() == "r":
        player_move = "Rock"
    elif player_move.lower() == "p":
        player_move = "Paper"
    elif player_move.lower() == "s":
        player_move = "Scissors"
    else:
        print(Fore.RED+"Invalid input! Please try again...")

    computer_move = ""
    computer_random_number = random.randint(1,3)

    if computer_random_number == 1:
        computer_move = "Rock"
    elif computer_random_number == 2:
        computer_move = "Paper"
    elif computer_random_number == 3:
        computer_move = "Scissors"

    if (player_move == "Rock" and computer_move == "Scissors") or \
    (player_move == "Paper" and computer_move == "Rock") or \
    (player_move == "Scissors" and computer_move == "Paper"):
        print(Fore.GREEN+"Congratulations! You Win!")
    elif player_move == computer_move:
        print(Fore.BLUE+"it's a Draw!")
    else:
        print(Fore.RED+"You Lose!")

print(Fore.YELLOW+"Lets play Rock Paper Scissors :)")
player_move = ""

game()

while player_move != "n":
    player_move = input(Fore.YELLOW+"Would you like to play again? [Y]es or [N]o: ")
    if player_move.lower() == "y":
        game()
    elif player_move.lower() == "n":
        print(Fore.YELLOW+"Bye, see you soon my friend!")
    else:
        print(Fore.RED+"Invalid input! Please try again...")

    
