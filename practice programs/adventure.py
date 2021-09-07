# text based adventure game 
# plan on paper

def start(): # define start
    print("You are standing in a shadowy room.")
    print("In the dim light you can make out 2 doors")
    print("Which one are you going to choose, left or right??")
    answer = input(">").lower() # make it lower so that you can ask if there is a l or r in it without missing Left or Right

    if "l" in answer:
        bear_room() # answer will send you to next function
    elif "r" in answer:
        monster_room()
    else:
        game_over("Too scared to choose?!")

def bear_room(): # define other functions in the same way
    print("You go through the door")
    print("There is a bear in here!")
    print("It is asleep, but has a pouch of gold laying beside it")
    print("Behind the bear is another door..")
    print("would you like to do: ")
    print("1 - creep quietly past the bear to the door")
    print("2 - Try and get the bag of gold before heading to the door.")
    print("3 - Head back the way you came.")
    answer = input(">")
    if answer == "1":
        print("Amazing, you managed to sneak past the bear through the door")
        diamond_room()
    elif answer == "2":
        game_over("You woke the bear and it ate you!")
    elif answer == "3":
        game_over("Scaredy cat.")
    else:
        game_over("Dont you know how to type a number?")

def monster_room():
    print("Woah, there is a monster in this room!")
    print("Luckily the hideous beast is asleep.")
    print("The door is behind the monster, you think you can get to it without waking the beast.")
    print("What would you like to do?")
    print("1 - Go through the door silently.")
    print("2 - Show your courage and save the local townspeople, kill the monster!!")
    print("3 - run away!!!!")
    answer = input(">")
    if answer == "1":
        print("You made it past without waking the monster!!")
        diamond_room()
    elif answer == "2":
        game_over("You tried to fight a monster? Are you kidding, of course it killed you!")
    elif answer == "3":
        game_over("Scaredy cat.")
    else:
        game_over("Dont you know how to type a number?")

def diamond_room():
    print("You made it through the door into a room filled with diamonds!")
    print("The room feels funny though, like the diamonds might be cursed!")
    print("Obviously there is a door to go through..")
    print("What would you like to do?")
    print("1 - Go through the door without touching anything")
    print("2 - Take some diamonds before you go.")
    print("3 - retrace your steps and get out of this crazy place")
    answer = input(">")
    if answer == "1":
        print("Well done, you realised touching those diamonds was a bad idea and gotten out of the building!")
        play_again()
    elif answer == "2":
        game_over("Obviously the diamonds were cursed... you've been turned into a slug")
    elif answer == "3":
        game_over("Scaredy cat.")
    else:
        game_over("Dont you know how to type a number?")

def game_over(reason):
    print("\n" + reason)
    print("Game Over")
    play_again()

def play_again():
    print("Do you want to play again???")
    answer = input(">").lower()
    if "y" in answer:
        start()
    else:
        exit()

start()
