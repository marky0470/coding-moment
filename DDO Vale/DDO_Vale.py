import random

class Button:
    
    def __init__(self):
        self.enabled = random.choice([0,1])

    def changeState(self):
        self.enabled ^= 1

class Board:

    def __init__(self, size):
        self.size = size
        self.buttons = [[Button() for i in range(size)] for j in range(size)]
        self.difficulty = int(input("Choose a difficulty:\n[0] Easy\n[1] Medium\n[2] Hard\n"))        
        self.isCardinal = True if self.difficulty == 0 else False
        self.isWon = False

        self.display()
        self.playing()

    def display(self):
        for i in self.buttons:
            for j in i:
                print("X" if j.enabled else "O", end=" ")
            print()

    def playing(self):
        while self.isWon == False:
            userInput = input("Coordinates or number of button\n")
            y,x = list(map(lambda x : x - 1, map(int, input("Coordinates of the button to press\n").split(','))))
            inputButton = self.buttons[x][y]
            inputButton.changeState()

            neighbors = []
            if self.isCardinal:
                neighborOffset = [[1,0],[-1,0],[0,1],[0,-1]]
            elif not self.isCardinal:
                neighborOffset = [[1,1],[-1,1],[-1,-1],[1,-1]]
            for offset in neighborOffset:
                buttonX = x+offset[0]
                buttonY = y+offset[1]
                if buttonX < 0 or buttonY < 0:
                    continue
                try:
                    neighbors.append(self.buttons[buttonX][buttonY])
                except IndexError:
                    pass

            for button in neighbors:
                button.changeState()

            if self.difficulty == 2:
                self.isCardinal = not(self.isCardinal)
            elif self.difficulty == 3:
                self.isCardinal = random.choice([True,False])

            self.display()

    def numToCoords(self, n):
        size = self.size
        x = n - (n // size) * size - 1
        y = int((n - (x + 1)) / size)
        return [y,x]

board = Board(input("Enter size of board: ")

