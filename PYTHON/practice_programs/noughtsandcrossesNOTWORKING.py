import random
number = random.randint(1,10) ## set the number variable as a number between 1 and 100
guess = None

class Game:
    def __init__(self):
        print("Welcome to noughts and crosses")
        print("Are you ready to play?")
        print("Good luck")

class turnnum(Game):

    def play(self):
        self.board = "_","_","_", "_","_","_", "_","_","_"
        self.boardnums = "1","2","3", "4","5","6", "7","8","9" 
        numBoard = ("\n".join(map(" ".join, zip(*[iter(self.board)] * 3))))
        self.choicesMade = []
        self.start()
        
        return numBoard, self.choicesMade

    def start(self):
        print("Which square would you like to put your x in??")
        print("Please pick a number 1 to 9 based of the chart")
        boardNumPos = ("\n".join(map(" ".join, zip(*[iter(self.boardnums)] * 3))))
        print(boardNumPos)
        self.choice = int(input(">"))
        if self.choice in range(1,10):
            self.turn1()
            return self.choice ## remember change back to return
        else:
            print("Thats not a valid number")
            exit()

    def mid_game(self):
        print("Which square would you like to put your x in??")
        print("Mid game - Please pick a number 1 to 9 based of the chart")
        boardNumPos = ("\n".join(map(" ".join, zip(*[iter(self.tempvarboard)] * 3))))
        print(boardNumPos) # YES 
        self.choice = int(input(">")) # YES
        if self.choice in range(1,10): # YES
            self.turn2() # YES
            return self.choice # YES
        else:
            print("Thats not a valid number")
            exit()

    def turn1(self):
        index = self.choice -1
        tempvarboard = list(self.boardnums)
        tempvarboard[index] = "-"
        self.tempvarboard = "".join(tempvarboard)
        
        boardNumPos = ("\n".join(map(" ".join, zip(*[iter(self.boardnums)] * 3))))
        #print(boardNumPos)

        tempvarchoice = list(self.board)
        tempvarchoice[index] = "X"
        self.tempvarchoice = "".join(tempvarchoice)
        choicePos = ("\n".join(map(" ".join, zip(*[iter(self.board)] * 3))))
        #print(choicePos)
        choiceString = str(self.choice)
        self.choicesMade = str(self.choicesMade)
        self.choicesMade = self.choicesMade + choiceString
        self.compchoice1()
        return self.tempvarchoice, self.tempvarboard, self.choicesMade
    
    def compchoice1(self):
        self.compChoice = random.choice([i for i in range(1,10) if i not in [self.choicesMade]]) 
        print(f"The computer chose position {self.compChoice}")
        
        indexC = (self.compChoice - 1)
        
        tempvarboard = list(self.tempvarboard)
        #print(self.tempvarboard)
        tempvarboard[indexC] = "-"
        self.tempvarboard = "".join(tempvarboard)
        #print(self.tempvarboard2)
        boardNumPos = ("\n".join(map(" ".join, zip(*[iter(self.tempvarboard)] * 3))))
        #print(boardNumPos)

        tempvarchoice = list(self.tempvarchoice)
        tempvarchoice[indexC] = "O"
        self.tempvarchoice = "".join(tempvarchoice)
        #print(self.tempvarchoice2)
        choicePos = ("\n".join(map(" ".join, zip(*[iter(self.tempvarchoice)] * 3))))
        print(choicePos)
        choiceStringComp = str(self.compChoice)
        self.choicesMade = str(self.choicesMade)
        self.choicesMade = self.choicesMade + choiceStringComp

        self.mid_game()
        return self.tempvarchoice, self.tempvarboard, self.choicesMade

        
    def turn2(self):
        index = self.choice -1
        tempvarboard = list(self.tempvarboard)
        tempvarboard[index] = "-"
        self.tempvarboard = "".join(tempvarboard)
        
        boardNumPos = ("\n".join(map(" ".join, zip(*[iter(self.boardnums)] * 3))))
        #print(boardNumPos)

        tempvarchoice = list(self.board)
        tempvarchoice[index] = "X"
        self.tempvarchoice = "".join(tempvarchoice)
        choicePos = ("\n".join(map(" ".join, zip(*[iter(self.tempvarboard)] * 3))))
        #print(choicePos)
        choiceString = str(self.choice)
        self.choicesMade = str(self.choicesMade)
        self.choicesMade = self.choicesMade + choiceString
        self.compchoice2()
        return self.tempvarchoice, self.tempvarboard, self.choicesMade

    def compchoice2(self):
        self.choicesMade 
        self.compChoice = random.choice([i for i in range(1,10) if i not in [self.choicesMade]]) 
        print(f"The computer chose position {self.compChoice}")
        #print(self.compChoice)
        indexC = (self.compChoice - 1)
        #print(f"index number {indexC}")
        #print(self.tempvarboard)
        #print(self.tempvarchoice)
        tempvarboard = list(self.tempvarboard)
        #print(self.tempvarboard)
        tempvarboard[indexC] = "-"
        self.tempvarboard = "".join(tempvarboard)
        #print(self.tempvarboard2)
        boardNumPos = ("\n".join(map(" ".join, zip(*[iter(self.tempvarboard)] * 3))))
        #print(boardNumPos)

        tempvarchoice = list(self.tempvarchoice)
        tempvarchoice[indexC] = "O"
        self.tempvarchoice = "".join(tempvarchoice)
        choicePos = ("\n".join(map(" ".join, zip(*[iter(self.tempvarchoice)] * 3))))
        print(choicePos)
        choiceStringComp = str(self.compChoice)
        self.choicesMade = str(self.choicesMade)
        self.choicesMade = self.choicesMade + choiceStringComp
        self.mid_game()
        return self.tempvarchoice, self.tempvarboard, self.choicesMade






        












go = turnnum()
go = go.play()