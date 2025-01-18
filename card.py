from score import Score
from enhancements import *

class Card:
    scores = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9, 
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11
    }

    def __init__(self, suit: str, rank: str, scoreboard: Score, enhancement: Enhancement = None):
        self.suit = suit
        self.rank = rank
        if enhancement is None:
            self.enhancement = BaseCard(scoreboard)
        else:
            self.enhancement = enhancement
        self.scoreboard = scoreboard
        self.number_of_triggers_on_hand = 1
        self.number_of_triggers_on_held = 1

    def isDiamondSuit(self):
        return (self.suit == "Diamond" or self.enhancement.isWildCard()) and not self.enhancement.isStoneCard()

    def isHeartSuit(self):
        return (self.suit == "Heart" or self.enhancement.isWildCard()) and not self.enhancement.isStoneCard()

    def isSpadeSuit(self):
        return (self.suit == "Spade" or self.enhancement.isWildCard()) and not self.enhancement.isStoneCard()

    def isClubSuit(self):
        return (self.suit == "Club" or self.enhancement.isWildCard()) and not self.enhancement.isStoneCard()

    def isFibonacciRank(self):
        return self.rank in ['2', '3', '5', '8', 'A']
    
    def isFaceCard(self):
        return self.rank in ['J', 'Q', 'K']
    
    def isEvenRank(self):
        return self.rank in ['2', '4', '6', '8', '10']
    
    def isOddRank(self):
        return self.rank in ['A', '3', '5', '7', '9']
    
    def is234or5Rank(self):
        return self.rank in ['2', '3', '4', '5']
    
    def isAceRank(self):
        return self.rank == 'A'

    def is4or10Rank(self):
        return self.rank in ['4', '10']
    
    def isKingRank(self):
        return self.rank == 'K'
    
    def isQueenRank(self):
        return self.rank == 'Q'

    def get_base_score(self):
        """ Devuelve el puntaje de la carta basado en su rango """
        return self.scores[self.rank]



    def trigger_base_effect(self):
        self.scoreboard.add_chips(self.get_base_score())
        #  Bonus chips van a caer aca también en un futuro

    def trigger_on_scored_jokers(self):
        """Aca se le va a bindear comportamiento de los jokers a las cartas para cuando puntueen."""
        pass

    def trigger_one_time_on_hand(self):
        # 3.1 Base effect (chips)
        self.trigger_base_effect()

        # 3.2 Card modifiers (only gold seal)

        # 3.3 On scored jokers.
        self.trigger_on_scored_jokers()


    def trigger_on_hand(self):
        """Trigguea todas las veces necesaria"""
        for _ in range(self.number_of_triggers_on_hand):
            self.trigger_one_time_on_hand()

    def increment_trigger_count_on_hand(self):
        self.number_of_triggers_on_hand += 1



    def trigger_on_held_jokers(self):
        """Aca se le va a bindear comportamiento de los jokers a las cartas para cuando se activen en mano."""
        pass


    def trigger_one_time_on_held(self):
        # 4.1 Enhancement (Steel card)
        self.trigger_on_held_enhancement()
        # 4.2 On held jokers.
        self.trigger_on_held_jokers()

    
    def trigger_on_held_enhancement(self):
        # The only on_held enhancement up to date is steel card bonus.
        self.enhancement.trigger_steel_bonus()


    def trigger_on_held(self):
        for _ in range(self.number_of_triggers_on_held):
            self.trigger_one_time_on_held()
    

    def increment_trigger_count_on_held(self):
        self.number_of_triggers_on_held += 1
