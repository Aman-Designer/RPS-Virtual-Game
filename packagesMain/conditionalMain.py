from packagesMain import functionMain, packageInit

def void(player, computer):
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