from src import text
from src import movement
class Tutorial:
    def __init__(self):
        self.tutorial = True
        self.words1 = text.Text(("In Time-Traveling Kangaroo, the objective is","to reach the end of time (AKA the end of the board).","On your turn, you will press the 'enter' key on your keyboard.", "(Press 'c' to continue to the next page or 'enter' to exit tutorial)"))
        self.words2 = text.Text(("You will also need to press 'enter' once you have","finished reading any text on the screen that does not have","other instructions. Once you have pressed 'enter' on your turn,","(Press 'c' to continue, 'a' to go back a page, or 'enter' to exit tutorial)"))
        self.words3 = text.Text(("you will receive an event card telling you how","many spaces to move in which direction, and how much KangaCash","you collect or lose. On spaces 7, 15, 27, and 32, you will encounter","(Press 'c' to continue, 'a' to go back a page, or 'enter' to exit tutorial)"))
        self.words4 = text.Text(("the shop, where you can purchase items. Most items","are single-use and will disappear after their effect has been triggered.","Decorations, pets, and headwear are game-long items, but only one","(Press 'c' to continue, 'a' to go back a page, or 'enter' to exit tutorial)"))
        self.words5 = text.Text(("of each may be equipped at any given time. If you","choose to change one of these game-long items, you must first discard","the item you currently have equipped. You may only have 3 items in your","(Press 'c' to continue, 'a' to go back a page, or 'enter' to exit tutorial)"))
        self.words6 = text.Text(("inventory at a time (this does not include equipped","items).","","(Press 'a' to go back a page or 'enter' to exit tutorial)"))
    def runtutorial(self,index):
        while self.tutorial == True:
            if index == 1:
                self.words1.usergiveinput()
                index = self.words1.choices()
                if index == 'c':
                    self.runtutorial(2)
                else:
                    self.tutorial = False
            elif index == 2:    
                self.words2.usergiveinput()
                index = self.words2.choices()
                if index == 'c':
                    self.runtutorial(3)
                elif index == 'a':
                    self.runtutorial(1)
                else:
                    self.tutorial = False
            elif index == 3:
                self.words3.usergiveinput()
                index = self.words3.choices()
                if index == 'c':
                    self.runtutorial(4)
                elif index == 'a':
                    self.runtutorial(2)
                else:
                    self.tutorial = False
            elif index == 4:
                self.words4.usergiveinput()
                index = self.words4.choices()
                if index == 'c':
                    self.runtutorial(5)
                elif index == 'a':
                    self.runtutorial(3)
                else:
                    self.tutorial = False
            elif index == 5:
                self.words5.usergiveinput()
                index = self.words5.choices()
                if index == 'c':
                    self.runtutorial(6)
                elif index == 'a':
                    self.runtutorial(4)
                else:
                    self.tutorial = False
            elif index == 6:
                self.words6.usergiveinput()
                index = self.words6.choices()
                if index == 'a':
                    self.runtutorial(5)
                else:
                    self.tutorial = False
        with open(r"etc\current_space.txt") as file:
            self.currentspace = int(file.read())
        while self.currentspace < 41:
            with open(r"etc\current_space.txt") as file:
                self.currentspace = int(file.read())
            m = movement.Movement()
            m.spaces()