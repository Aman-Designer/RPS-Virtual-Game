from random import randint

from packagesMain import packageInit

def main(status):
    print("You have", status, "would you like to play again?")
    choice = input("Y / N?")
    if choice == "N" or choice == "n":
        print("You have chose to exit. See you next time!")
        exit()
    elif choice == "Y" or choice == "y":
        print("You have chose to continue, let's see if you win this time!")
        global player_lives
        global computer_lives
        global total_lives
            
        packageInit.player_lives = packageInit.total_lives
        packageInit.computer_lives = packageInit.total_lives
    else:
        packageInit.player = False

print("++++++ Welcome to the Legendary Rock Paper Scissors Game ++++++\n")

while packageInit.player == False:

    print("****************************************************************")
    print("You have", packageInit.player_lives, "left out of", packageInit.total_lives)
    print("The computer has", packageInit.computer_lives, "left out of", packageInit.computer_lives)
    print("****************************************************************\n")
    print("Choose from the options or enter q to exit!")
    packageInit.player = input("Rock, Paper, Scissors?\n")

    if packageInit.player == "q":
        print("You have chosen to quite the game! BYE!")
        print("===Goodluck in your future endeavors===")
        exit()

    packageInit.computer = packageInit.options[randint(0,2)]

    print("\nTina chose", packageInit.player)
    print("=========================")
    print("Computer chose", packageInit.computer, "\n")

    if packageInit.player == packageInit.computer:
        print("===================")
        print("Tie! No lives lost!")
        print("===================\n")
    elif packageInit.player == "Rock":
        if packageInit.computer == "Paper":
            print("I thought Tina never looses, but you lost from a computer!", packageInit.computer, "covers", packageInit.player,"\n")
            packageInit.player_lives -= 1
        else:
            print("Tina has won the great battel!", packageInit.player, "smashes", packageInit.computer, "\n")
            packageInit.computer_lives -= 1

    elif packageInit.player == "Paper":
        if packageInit.computer == "Scissors":
            print("Don't worry Tina, I'm sure you'll win next time.", packageInit.computer, "cut", packageInit.player, "\n")
            packageInit.player_lives -= 1
        else:
            print("The almighty Tina wins!!", packageInit.player, "covers", packageInit.computer, "\n")
            packageInit.computer_lives -= 1

    elif packageInit.player == "Scissors":
        if packageInit.computer == "Rock":
            print("I'm sorry you have lost to a computer :(", packageInit.computer, "smashes", packageInit.player, "\n")
            packageInit.player_lives -= 1
        else:
            print("You're the Leonidas to the Sparta, GLORY!", packageInit.player, "cut", packageInit.computer, "\n")
            packageInit.computer_lives -= 1

    else:
        print("That's not a valid play. Check your spelling or Punctuation!")

    if packageInit.player_lives == 0:
        main("lost")

    if packageInit.computer_lives == 0:
        main("won")

    packageInit.player = False
    computer = packageInit.options[randint(0,2)]