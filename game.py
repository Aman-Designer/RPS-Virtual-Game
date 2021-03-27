from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

computer_lives = 3
player_lives = 3
total_lives =3

player = False

while player == False:

    player = input("Choose form Rock, Paper, Scissors?")

    print("Tina chose", player)
    print("Computer chose", computer)

    if player == computer:
        print("Tie! No lives lost!")
    elif player == "Rock":
        if computer == "Paper":
            print("I thought Tina never looses, but you lost from a computer!", computer, "covers", player,)
            player_lives -= 1
            print("Player Lives=", player_lives, "Computer Lives=", computer_lives)
        else:
            print("Tina wins!", player, "smashes", computer)
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
        player = True
        print("You have faced your defeat")
    else:
        player = False

    if computer_lives == 0:
            player = True
            print("The computer was bound to loose")
    else:
        player = False
    computer = t[randint(0,2)]