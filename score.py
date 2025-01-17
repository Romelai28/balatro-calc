class Score:
    def __init__(self):
        self.chips = 0
        self.mult = 1

    def add_chips(self, amount):
        self.chips += amount
    
    def add_mult(self, amount):
        self.mult += amount

    def times_mult(self, amount):
        self.mult *= amount

    def final_score(self):
        return self.chips * self.mult