from random import randint

from packagesMain import packageInit, functionMain, conditionalMain

print("++++++ Welcome to the Legendary Rock Paper Scissors Game ++++++\n")

while packageInit.player == False:

    print("****************************************************************")
    print("You have", packageInit.player_lives, "left out of", packageInit.total_lives)
    print("The computer has", packageInit.computer_lives, "left out of", packageInit.total_lives)
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

    conditionalMain.void(packageInit.player, packageInit.computer)

    if packageInit.player_lives == 0:
        functionMain.main("lost")

    if packageInit.computer_lives == 0:
        functionMain.main("won")

    packageInit.player = False
    computer = packageInit.options[randint(0,2)]