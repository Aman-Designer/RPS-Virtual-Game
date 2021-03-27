from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

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

while player == False:

    print("Tina chose", player)
    print("Computer chose", computer)

    print("Choose from the options or enter q to exit!")

    player = input("Choose form Rock, Paper, Scissors?\n")

    if player == "q":
        print("You have chosen to quite the game! BYE!")
        exit()

    if player == computer:
        print("Tie! No lives lost!")
    elif player == "Rock":
        if computer == "Paper":
            print("I thought Tina never looses, but you lost from a computer!", computer, "covers", player)
            player_lives -= 1
            print("Player Lives=", player_lives, "Computer Lives=", computer_lives)
        else:
            print("Tina has won the great battel!", player, "smashes", computer)
            computer_lives -= 1
            print("Player Lives=", player_lives, "Computer Lives=", computer_lives)

    elif player == "Paper":
        if computer == "Scissors":
            print("Don't worry Tina, I'm sure you'll win next time.", computer, "cut", player)
            player_lives -= 1
            print("Player Lives=", player_lives, "Computer Lives=", computer_lives)
        else:
            print("The almighty Tina wins!!", player, "covers", computer)
            computer_lives -= 1
            print("Player Lives=", player_lives, "Computer Lives=", computer_lives)

    elif player == "Scissors":
        if computer == "Rock":
            print("I'm sorry you have lost to a computer :(", computer, "smashes", player)
            player_lives -= 1
            print("Player Lives=", player_lives, "Computer Lives=", computer_lives)
        else:
            print("You're the Leonidas to the Sparta, GLORY!", player, "cut", computer)
            computer_lives -= 1
            print("Player Lives=", player_lives, "Computer Lives=", computer_lives)

    else:
        print("That's not a valid play. Check your spelling or Punctuation!")

    if player_lives == 0:
        main("lost")

    if computer_lives == 0:
        main("won")

    player = False
    computer = t[randint(0,2)]