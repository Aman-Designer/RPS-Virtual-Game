from packagesMain import packageInit

def main(status):
    print("You have", status, "would you like to play again?")
    choice = input("Y / N?")
    if choice == "N" or choice == "n":
        print("You have chose to exit. See you next time!")
        exit()
    elif choice == "Y" or choice == "y":
        print("You have chose to continue, let's see if you win this time!")
   
        packageInit.player_lives = packageInit.total_lives
        packageInit.computer_lives = packageInit.total_lives
        packageInit.player = False
    else:
        packageInit.player = False