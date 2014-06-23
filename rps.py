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
    
