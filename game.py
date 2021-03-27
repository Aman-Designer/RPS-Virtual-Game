from random import randint

options = ["Rock", "Paper", "Scissors"]
computer = options[randint(0,2)]
computer_lives = 2
player_lives = 2
total_lives = 2
player = False

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
            
        player_lives = total_lives
        computer_lives = total_lives
    else:
        player = False

print("++++++ Welcome to the Legendary Rock Paper Scissors Game ++++++\n")

while player == False:

    print("****************************************************************")
    print("You have", player_lives, "left out of", total_lives)
    print("The computer has", computer_lives, "left out of", computer_lives)
    print("****************************************************************\n")
    print("Choose from the options or enter q to exit!")
    player = input("Rock, Paper, Scissors?\n")

    if player == "q":
        print("You have chosen to quite the game! BYE!")
        print("===Goodluck in your future endeavors===")
        exit()

    print("\nTina chose", player)
    print("=========================")
    print("Computer chose", computer, "\n")

    if player == computer:
        print("===================")
        print("Tie! No lives lost!")
        print("===================\n")
    elif player == "Rock":
        if computer == "Paper":
            print("I thought Tina never looses, but you lost from a computer!", computer, "covers", player,"\n")
            player_lives -= 1
        else:
            print("Tina has won the great battel!", player, "smashes", computer, "\n")
            computer_lives -= 1

    elif player == "Paper":
        if computer == "Scissors":
            print("Don't worry Tina, I'm sure you'll win next time.", computer, "cut", player, "\n")
            player_lives -= 1
        else:
            print("The almighty Tina wins!!", player, "covers", computer, "\n")
            computer_lives -= 1

    elif player == "Scissors":
        if computer == "Rock":
            print("I'm sorry you have lost to a computer :(", computer, "smashes", player, "\n")
            player_lives -= 1
        else:
            print("You're the Leonidas to the Sparta, GLORY!", player, "cut", computer, "\n")
            computer_lives -= 1

    else:
        print("That's not a valid play. Check your spelling or Punctuation!")

    if player_lives == 0:
        main("lost")

    if computer_lives == 0:
        main("won")

    player = False
    computer = options[randint(0,2)]