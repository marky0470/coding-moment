import random

class Button:
    
    def __init__(self):
        self.enabled = random.choice([0,1])

    def changeState(self):
        self.enabled ^= 1

class Board:

    def __init__(self, size):
        self.size = int(size)
        self.buttons = [[Button() for i in range(size)] for j in range(size)]
        self.difficulty = int(input("Choose a difficulty:\n[0] Easy\n[1] Medium\n[2] Hard\n[3] Random"))        
        self.direction = True if self.difficulty == 0 else False

        print("You may input either the number of the button you wish to press or its coordinate starting from 1")
        print("[1][2][3]\n[4][5][6]\n[7][8][9]")
        print("OR")
        print("[1,1][2,1][3,1]\n[1,2][2,2][3,2]\n[1,3][2,3][3,3]")

        self.display()
        self.playing()

    def display(self):
        for i in self.buttons:
            for j in i:
                print("X" if j.enabled else "O", end=" ")
            print()

    def checkComplete(self):
        for i in self.buttons:
            for j in i:
                if j.enabled == False:
                    return False
        return True

    def playing(self):
        while self.checkComplete() == False:
            user_input = input("Coordinates or number of button\n")
            try:
                y,x = list(map(lambda x : x - 1, map(int, user_input.split(','))))
            except:
                y,x = self.numToCoords(int(user_input))
            input_button = self.buttons[x][y]
            input_button.changeState()

            if self.direction:
                neighbor_offset = [[1,0],[-1,0],[0,1],[0,-1]]
            elif not self.direction:
                neighbor_offset = [[1,1],[-1,1],[-1,-1],[1,-1]]
            for offset in neighbor_offset:
                button_x = x+offset[0]
                button_y = y+offset[1]
                if button_x in range(self.size) and button_y in range(self.size):
                    self.buttons[button_x][button_y].changeState()
                else:
                    pass

            if self.difficulty == 2:
                self.direction = not(self.direction)
            elif self.difficulty == 3:
                self.direction = random.choice([True,False])

            self.display()

        print("Complete")

    def numToCoords(self, n):
        size = self.size
        x = n - (n // size) * size - 1
        y = int((n - (x + 1)) / size)
        return [y,x]

board = Board(int(input("Enter size of board: ")))
