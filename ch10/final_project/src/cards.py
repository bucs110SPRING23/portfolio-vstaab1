import random
card_name = [
    "Whirly Bird",
    "Blackout",
    "New Pair of Thongs",
    "Cryo Machine",
    "Wombat Encounter",
    "Butcher",
    "42 Wallaby Way, Sydney",
    "Rockin' with it",
    "Canceled",
    "Bludge Around the House",
    "Postie",
    "Snaggs",
    "The Great Emu War",
    "Shrimp on the Barbie",
    "Opera",
    "Dingo Encounter",
    "New New Perth",
    "Kangaroo Revolution",
    "Boomerang",
    "Wildfire"
]
card_space = {
    "Wildfire": 2,
    "Boomerang": 2,
    "Whirly Bird":-1,
    "Blackout":2,
    "New Pair of Thongs":3,
    "Cryo Machine":5,
    "Wombat Encounter":2,
    "Butcher":1,
    "42 Wallaby Way, Sydney":-1,
    "Rockin' with it":-1,
    "Canceled":-2,
    "Bludge Around the House":0,
    "Postie":4,
    "Snaggs":1,
    "The Great Emu War":-2,
    "Shrimp on the Barbie":2,
    "Opera":1,
    "Dingo Encounter":2,
    "New New Perth":4,
    "Kangaroo Revolution":3
}
card_money = {
    "Wildfire":-20,
    "Boomerang":10,
    "Whirly Bird":-10,
    "Blackout":-10,
    "New Pair of Thongs":10,
    "Cryo Machine":10,
    "Wombat Encounter":10,
    "Butcher":-10,
    "42 Wallaby Way, Sydney":20,
    "Rockin' with it":30,
    "Canceled":-20,
    "Bludge Around the House":-10,
    "Postie":30,
    "Snaggs":-10,
    "The Great Emu War":20,
    "Shrimp on the Barbie":20,
    "Opera":10,
    "Dingo Encounter":0,
    "New New Perth":20,
    "Kangaroo Revolution":20
}
card_description = {
    "Snaggs":("You go forward in time to eat some awesome sausages. ","Advance one space and lose 10 KangaCash","",""),
    "New Pair of Thongs":("You find some cool flipflops and decide to wear them in ","the future. Everyone loves them and wants to be your friend. ","Advance three spaces and gain 10 KangaCash",""),
    "Whirly Bird":("A helicopter crashes into your time machine. Lose ","10 KangaCash and fall back one space.","",""),
    "Blackout":("The power goes out in your time machine as you travel ","forward in time. You crash land 300 years before expected.","Advance two spaces and lose 10 KangaCash.",""),
    "Cryo Machine":("You fall into a cryo machine and wake up 1,000 years ","in the future. Advance five spaces and collect 10 KangaCash.","",""),
    "Wombat Encounter":("A wombat appears. He gives you a turbo engine ","attachment for your time machine. Advance two spaces ", "and gain 10 KangaCash.",""),
    "Butcher":("A butcher chases you, and you hastily escape by going ","forward in time. Advance one space and lose 10 KangaCash.","",""),
    "42 Wallaby Way, Sydney":("You go back in time to help a clownfish ","find his son. Go back one space and gain 20 KangaCash.","",""),
    "Rockin' with it":("You go back in time to audition for AC/DC. Go back ","one space and collect 30 KangaCash.","",""),
    "Canceled":("You accidentally become the world's most hated kangaroo. ","Go back two spaces and lose 20 KangaCash.","",""),
    "Bludge Around the House":("You don't want to do anything today. No ","advancement and lose 10 KangaCash.","",""),
    "Kangaroo Revolution":("You start a kangaroo revolution and travel ","forward in time to see the progress. Everything has gone as","planned. Advance three spaces and gain 20 KangaCash.",""),
    "Postie":("You receive an inheritence letter in the mail. You invest ","it and travel forward in time to collect the interest. ","Advance four spaces and collect 30 Kangacash.",""),
    "The Great Emu War":("You travel back in time to fight in the Great Emu ","War. You win. Go back two spaces and collect 20 KangaCash.","",""),
    "Shrimp on the Barbie":("You create an amazing barbecue sauce and travel ","forward in time to collect your royalties. Advance two","spaces and collect 20 KangaCash.",""),
    "Opera":("Someone named 'Sydney O. House' wants you to perform opera","in a few years. Advance one space and collect 10 KangaCash.","",""),
    "Dingo Encounter":("You escape a dingo by traveling into the future. Advance ","two spaces. No changes to KangaCash.","",""),
    "New New Perth":("You travel into the future to see Perth rebuilt after the ","Western Australian uprising of 2799. Advance four","spaces and collect 20 KangaCash.",""),
    "Boomerang":("While visiting the past, you find a magical boomerang that","shoots you forward in time. Advance two spaces","and collect 10 KangaCash.",""),
    "Wildfire":("A horrible fire breaks out and you barely make it out","alive by going forward in time. Advance two spaces","and lose 20 KangaCash.","")
}
class Card:
    def __init__(self):
        self.length = len(card_name)
        self.pick = random.randrange(0,self.length)
        self.card = card_name[self.pick]
        with open(r"etc\current_space.txt") as file:
            self.current_space = int(file.read())
        if self.current_space <= 2:
            if card_space[self.card] < 0:
                while card_space[self.card] < 0:
                    self.pick = random.randrange(0,self.length)
                    self.card = card_name[self.pick]
        self.spaces = card_space[self.card]
        self.description = card_description[self.card]
        self.money = card_money[self.card]
        self.current_space = self.current_space
    def cardpick(self):
        return str(self.card)
    def cardspaces(self):
        return int(self.spaces)
    def carddescription(self):
        return list(self.description)
    def cardsmoney(self):
        return int(self.money)
    def currentspace(self):
        return int(self.current_space)