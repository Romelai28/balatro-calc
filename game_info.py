class GameInfo:
    def __init__(self, remaining_hands = 3, remaining_discards = 3, joker_slots = 5, money = 0):
        self.remaining_hands = remaining_hands
        self.remaining_discards = remaining_discards
        self.joker_slots = joker_slots
        self.money = money
    
    def isFinalHand(self):
        return self.remaining_hands == 1
