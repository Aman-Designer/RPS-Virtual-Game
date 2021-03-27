from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:

    player = input("Choose form Rock, Paper, Scissors?")

    print("Tina chose", player)
    print("Computer chose", computer)

    if player == computer:
        print("Tie!")
    elif player == "Rock":

        if computer == "Paper":
            print("I thought Tina never looses, but you lost from a computer!", computer, "covers", player)
        else:
            print("Tina wins!", player, "smashes", computer)
    elif player == "Paper":

        if computer == "Scissors":
            print("Don't worry Tina, I'm sure you'll win next time.", computer, "cut", player)
        else:
            print("Tina wins!", player, "covers", computer)
    elif player == "Scissors":

        if computer == "Rock":
            print("You're the Leonidas to the Sparta, GLORY!", computer, "smashes", player)
        else:
            print("Tina wins!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling or Punctuation!")

    player = False
    computer = t[randint(0,2)]