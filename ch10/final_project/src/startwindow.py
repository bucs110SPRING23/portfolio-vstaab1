from src import text
from src import username
from src import tutorial
from src import movement
class Start:
    def __init__(self):
        with open(r"etc\current_space.txt","w") as file:
            file.write("0")
        self.words1 = text.Text(("Welcome to Time-Traveling Kangaroo","","","Press 'enter' at any time to continue"))
        self.words2 = text.Text(("Please enter your name","","",""))
        self.words4 = text.Text(("Would you like to view the tutorial?","","Press 'y' to view the tutorial,","or press 'n' to skip the tutorial."))
    def start(self):
        with open(r"etc\KangaCash.txt","w") as file1:
            file1.write("20")
        self.words1.regulartext("True")
        self.words2.regulartext("False")
        user = username.Username()
        user.takename()
        self.name = str(user.username())
        self.words3 = text.Text(("Welcome, " + self.name + "!","","",""))
        self.words3.regulartext("True")
        self.tutorialask()
    def tutorialask(self):
        self.words4.usergiveinput()
        self.decision = self.words4.choices()
        if self.decision == "y":
            t = tutorial.Tutorial()
            t.runtutorial(1)
        elif self.decision == "n":
            with open(r"etc\current_space.txt") as file:
                self.currentspace = int(file.read())
            while self.currentspace < 41:
                m = movement.Movement()
                m.spaces()
                with open(r"etc\current_space.txt") as file:
                    self.currentspace = int(file.read())
        else:
            words = text.Text(("Sorry, that was an invalid response.","Please try again","","Press 'enter' to continue."))
            words.usergiveinput()
            self.decision = words.choices()
            self.tutorialask()

