def compare(choice1, choice2):
    """play rock, paper, scissors"""
    if choice1 == choice2:
        print("Tie!")
    elif choice1 == 'rock':
        if choice2 == 'scissors':
            print("rock wins")
    elif choice1 == 'rock':
        if choice2 == 'paper':
            print("paper wins")
    elif choice1 == 'scissors':
        if choice2 == 'paper':
            print("scissors wins")
    elif choice1 == 'scissors':
        if choice2 == 'rock':
            print("rock wins")
    elif choice1 == 'paper':
        if choice2 == 'rock':
            print("paper wins")
    elif choice1 == 'paper':
        if choice2 == 'scissors':
            print("scissors wins")

rounds = int(raw_input("enter number of rounds"))
player1_name = raw_input("enter player1 name: ")
player2_name = raw_input("enter player2 name: ")
counter = 0
while counter != rounds:
    choice1 = choice()
    choice2 = choice()
    choice3 = choice()
    compare(choice1, choice2)
    counter +=1
print ("{} and {} would you like to play again?".format(player1_name, player2_name))
