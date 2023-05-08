class Player:
    def __init__(self, pnum):
        self.player_num = pnum
        self.hit_range = 2
        self.health = 10
        self.is_large = False
        self.lives = 3
class Block:
    def __init__(self):
        self.size = (30,30,30,30)
        self.ycoord = 100
        self.activated = False
class Enemy:
    def __init__(self, x):
        self.health = 1 + x
        self.hit_range = 1 + x
        self.is_large = False