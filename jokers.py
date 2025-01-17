from hand import HandToPlay
from score import Score
from editions import *

class JokersClass:
    def __init__(self, hand_to_play: HandToPlay, scoreboard: Score, edition: Editions):
        self.hand_to_play = hand_to_play
        self.scoreboard = scoreboard
        self.edition = edition

    def trigger_foil_and_holographic_bonus(self):
        self.edition.trigger_foil_and_holographic_bonus()

    def trigger_polychrome_bonus(self):
        self.edition.trigger_polychrome_bonus()
    
    def on_played(self):
        pass

    def bind_on_score(self):
        pass
    
    def on_held(self):
        pass
    
    def trigger_independent(self):
        pass

    def passive(self):
        pass

# 1
class Joker(JokersClass):
    """+4 mult"""
    def trigger_independent(self):
        self.scoreboard.add_mult(4)


# 2
class GreedyJoker(JokersClass):
    """Played cards with Diamond suit give +3 Mult when scored"""
    def bind_on_score(self):
        for card in self.hand_to_play.card_that_will_score():
            if card.isDiamondSuit():

                def decorator(method_trigger_on_hand):
                    def wrapper():
                        # Lineas antes
                        method_trigger_on_hand()
                        # Lineas dps
                        self.scoreboard.add_mult(3)
                    return wrapper

                card.trigger_on_hand = decorator(card.trigger_on_hand)


# 3
class LustyJoker(JokersClass):
    """Played cards with Heart suit give +3 Mult when scored"""
    def bind_on_score(self):
        for card in self.hand_to_play.card_that_will_score():
            if card.isHeartSuit():

                def decorator(method_trigger_on_hand):
                    def wrapper():
                        # Lineas antes
                        method_trigger_on_hand()
                        # Lineas dps
                        self.scoreboard.add_mult(3)
                    return wrapper

                card.trigger_on_hand = decorator(card.trigger_on_hand)


# 4
class WrathfulJoker(JokersClass):
    """Played cards with Spade suit give +3 Mult when scored"""
    def bind_on_score(self):
        for card in self.hand_to_play.card_that_will_score():
            if card.isSpadeSuit():

                def decorator(method_trigger_on_hand):
                    def wrapper():
                        # Lineas antes
                        method_trigger_on_hand()
                        # Lineas dps
                        self.scoreboard.add_mult(3)
                    return wrapper

                card.trigger_on_hand = decorator(card.trigger_on_hand)    


# 5
class GluttonousJoker(JokersClass):
    """Played cards with Club suit give +3 Mult when scored """
    def bind_on_score(self):
        for card in self.hand_to_play.card_that_will_score():
            if card.isClubSuit():

                def decorator(method_trigger_on_hand):
                    def wrapper():
                        # Lineas antes
                        method_trigger_on_hand()
                        # Lineas dps
                        self.scoreboard.add_mult(3)
                    return wrapper

                card.trigger_on_hand = decorator(card.trigger_on_hand)    


# 6
class JollyJoker(JokersClass):
    """+8 Mult if played hand contains a Pair"""
    def trigger_independent(self):
        if self.hand_to_play.constainsPair:
            self.scoreboard.add_mult(8)


# 7
class ZanyJoker(JokersClass):
    """+12 Mult if played hand contains a Three of a Kind"""
    def trigger_independent(self):
        if self.hand_to_play.constainsThreeOfAKind:
            self.scoreboard.add_mult(12)


#8
class MadJoker(JokersClass):
    """+10 Mult if played hand contains a Two Pair"""
    def trigger_independent(self):
        if self.hand_to_play.constainsTwoPair:
            self.scoreboard.add_mult(10)


#9
class CrazyJoker(JokersClass):
    """+12 Mult if played hand contains a Straight"""
    def trigger_independent(self):
        if self.hand_to_play.constainsStraight:
            self.scoreboard.add_mult(12)


#10
class DrollJoker(JokersClass):
    """+10 Mult if played hand contains a Flush"""
    def trigger_independent(self):
        if self.hand_to_play.constainsFlush:
            self.scoreboard.add_mult(10)


#11