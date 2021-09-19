import random # import random so you can get the computer to choose rock paper or scissors
computer_choices = ["rock", "paper", "scissors"] # the things for the computer to select from

wins = 0
losses = 0
ties = 0
counter = 0
games = " "

def start():
    global counter, ties, losses, wins, games
    print("Lets play rock, paper scissors!")
    print("Would you like to play best of 3 or 5? ")
    games = str((input(">")))
    print("3....")
    print("2....")
    print("1....")
    print("GO!")
    #print("what do you choose?")
    #answer = input(">").lower()
    #counter = 0
    if "5" in games:
        games = ("1","2","3","4","5")
        in_game()
        return games, wins, losses, ties
    elif "3" in games:
        games = ("1","2","3")
        in_game() 
        return games, wins, losses, ties
    else:
        print("selection error") 
    return counter, ties, losses, wins, games 

def in_game():
    global counter, ties, losses, wins, games
    
    while counter < len(games): #while counter <= games:
        print("what do you choose?")
        answer = input(">").lower()
        if "rock" in answer:
            rock() # answer will send you to next function
        elif "paper" in answer:
            paper()
        elif "scissors" in answer:         
            scissors()
        else:
            print("Would you like to play again?")
            play_again()
        return counter, ties, losses, wins, games
    


def rock():
    global counter, ties, losses, wins
    comp = random.sample(computer_choices, k=1)
    print(f"Computer chooses {comp}...") # Computer chooses ['scissors']... --> how to get rid of the brackets?
    if "rock" in comp:
        print("Two rock tie!")
        counter += 1
        ties += 1
        in_game()
        #play_again()
    elif "paper" in comp:
        print("Paper covers rock! You lose")
        counter += 1
        losses += 1
        in_game()
        #play_again()
    elif "scissors" in comp:
        print("Rock dulls scissors! Winner")
        counter += 1
        wins += 1
        in_game()
    else: #comp == "scissors":
        print("no match error")
        #print("Rock dulls scissors! Winner ROCK ERROR")
        #counter += 1
        #wins += 1
        #in_game()
            #play_again()
    return counter, ties, losses, wins, games

def paper():
    global counter, ties, losses, wins
    comp = random.sample(computer_choices, k=1)
    print(f"Computer chooses {comp}...")
    if "paper" in comp:
        print("Two sheets of paper!")
        counter += 1
        ties += 1
        in_game()
        #play_again()
    elif "rock" in comp:
        print("Paper covers rock! You Win")
        counter += 1
        wins += 1
        in_game()
        #play_again()
    elif "scissors" in comp:
        print("Scissors cut paper, you lose ")
        counter += 1
        losses += 1
        in_game()
    else: # comp == "scissors":
        print("no match error")
        
    return counter, ties, losses, wins, games

def scissors():
    global counter, ties, losses, wins
    comp = random.sample(computer_choices, k=1)
    print(f"Computer chooses {comp}...")
    if "scissors" in comp:
        print("Two pairs of scissors!")
        counter += 1
        ties += 1
        in_game()
        #play_again()
    elif "rock" in comp:
        print("Rock dulls scissors, you lose ")
        counter += 1
        losses += 1
        in_game()
    elif "paper" in comp:
        print("Scissors cut paper, you win!")
        counter += 1
        wins += 1
        in_game()
            #play_again()
    else: # comp == "paper":
        print("no match error")
        #print("Scissors cut paper, you win!")
    
    return counter, ties, losses, wins, games
    
    

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
wins = (wins)
losses = (losses)
ties = (ties)
count = (counter)

print(f"You won {wins} games, lost {losses} and drew {ties}, you played {count} games" )


    