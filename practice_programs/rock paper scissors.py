import random
computer_choices = ["rock", "paper", "scissors"]

def start():
    print("Lets play rock, paper scissors!")
    print("3....")
    print("2....")
    print("1....")
    print("GO!")
    print("what do you choose?")
    answer = input(">").lower()

    if "rock" in answer:
        rock() # answer will send you to next function
    elif "paper" in answer:
        paper()
    elif "scissors" in answer:
        scissors()
    else:
        game_over("Can't you spell??")

def rock():
    comp = random.sample(computer_choices, k=1)
    print(f"Computer chooses {comp}...") # Computer chooses ['scissors']... --> how to get rid of the brackets?
    if comp == "rock":
        print("Two rock tie!")
        play_again()
    elif comp == "paper":
        print("Paper covers rock! You lose")
        play_again()
    else: #comp == "scissors":
        print("Rock dulls scissors! Winner")
        play_again()

def paper():
    comp = random.sample(computer_choices, k=1)
    print(f"Computer chooses {comp}...")
    if comp == "paper":
        print("Two sheets of paper!")
        play_again()
    elif comp == "rock":
        print("Paper covers rock! You Win")
        play_again()
    else: # comp == "scissors":
        print("Scissors cut paper, you lose")
        play_again()

def scissors():
    comp = random.sample(computer_choices, k=1)
    print(f"Computer chooses {comp}...")
    if comp == "scissors":
        print("Two pairs of scissors!")
        play_again()
    elif comp == "rock":
        print("Rock dulls scissors, you lose")
        play_again()
    else: # comp == "paper":
        print("Scissors cut paper, you win!")
        play_again()
    
def play_again():
    print("Do you want to play again?")
    playanswer = input(">").lower()
    if "yes" in playanswer:
        start()
    elif "no" in playanswer:
        print("No worries, see you again next time")
        exit()        
    else:
        print("Sorry, I didnt understand that")
        play_again() ## this sends it back to the top of the function if they misspell yes or no        
start()


    