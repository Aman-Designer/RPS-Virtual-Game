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