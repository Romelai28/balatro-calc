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

    
    def bind_on_score_generic(self, condition, codigo_a_agregar):
        for card in self.hand_to_play.card_that_will_score():
            if condition(card):

                def decorator(old_method_trigger_on_hand):
                    def wrapper():
                        # Lineas antes
                        old_method_trigger_on_hand()
                        # Lineas dps
                        codigo_a_agregar()
                    return wrapper

                card.trigger_on_hand = decorator(card.trigger_on_hand)



# 1
class Joker(JokersClass):
    """+4 mult"""
    def trigger_independent(self):
        self.scoreboard.add_mult(4)


# 2
class GreedyJoker(JokersClass):
    """Played cards with Diamond suit give +3 Mult when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isDiamondSuit, lambda: self.scoreboard.add_mult(3))


# 3
class LustyJoker(JokersClass):
    """Played cards with Heart suit give +3 Mult when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isHeartSuit, lambda: self.scoreboard.add_mult(3))


# 4
class WrathfulJoker(JokersClass):
    """Played cards with Spade suit give +3 Mult when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isSpadeSuit, lambda: self.scoreboard.add_mult(3))


# 5
class GluttonousJoker(JokersClass):
    """Played cards with Club suit give +3 Mult when scored """
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isClubSuit, lambda: self.scoreboard.add_mult(3))


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
class SlyJoker(JokersClass):
    """+50 Chips if played hand contains a Pair"""
    def trigger_independent(self):
        if self.hand_to_play.constainsPair:
            self.scoreboard.add_chips(50)


#12
class WilyJoker(JokersClass):
    """+100 Chips if played hand contains a Three of a Kind"""
    def trigger_independent(self):
        if self.hand_to_play.constainsThreeOfAKind:
            self.scoreboard.add_chips(100)


#13
class CleverJoker(JokersClass):
    """+80 Chips if played hand contains a Two Pair"""
    def trigger_independent(self):
        if self.hand_to_play.constainsTwoPair:
            self.scoreboard.add_chips(80)


#14
class DeviousJoker(JokersClass):
    """+100 Chips if played hand contains a Straight"""
    def trigger_independent(self):
        if self.hand_to_play.constainsStraight:
            self.scoreboard.add_chips(100)


#15
class CraftyJoker(JokersClass):
    """+80 Chips if played hand contains a Flush"""
    def trigger_independent(self):
        if self.hand_to_play.constainsFlush:
            self.scoreboard.add_chips(80)


#16
class HalfJoker(JokersClass):
    """+20 Mult if played hand contains 3 or fewer cards. """
    def trigger_independent(self):
        if self.hand_to_play.playingHandSize() <= 3:
            self.scoreboard.add_mult(20)


#17 TODO: agregar un contador de cuantos joker slot tengo.
#18
#19


#20
class CreditCard(JokersClass):
    """Go up to -$20 in debt"""
    pass


#21
class CeremonialDagger(JokersClass):
    """When Blind is selected, destroy Joker to the right and permanently add double its sell value to this Mult (Currently +0 Mult)"""
    def __init__(self, hand_to_play, scoreboard, edition, mult_value = 0):
        super().__init__(hand_to_play, scoreboard, edition)
        self.mult_value = mult_value
    
    def trigger_independent(self):
        self.scoreboard.add_mult(self.mult_value)


#22
#23


#24
class MarbleJoker(JokersClass):
    """Adds one Stone card to the deck when Blind is selected"""
    pass


#25


#26
#27
#28
#29


#30
class ChaosTheClown(JokersClass):
    """1 free Reroll per shop"""
    pass


#31
class Fibonacci(JokersClass):
    """Each played Ace, 2, 3, 5, or 8 gives +8 Mult when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isFibonacciRank, lambda: self.scoreboard.add_mult(8))


#32
#33
#34
#35
#36
#37
#38
#39
#40
#41
#42
#43
#44
#45
#46
#47
#48
#49
#50
#51
#52
#53
#54
#55
#56
#57
#58
#59
#60
#61
#62
#63
#64
#65
#66
#67
#68
#69
#70
#71
#72
#73
#74
#75
#76
#77
#78
#79
#80
#81
#82
#83
#84
#85
#86
#87
#88
#89
#90
#91
#92
#93
#94
#95
#96
#97
#98
#99
#100
#101
#102
#103
#104
#105
#106
#107
#108
#109
#110
#111
#112
#113
#114
#115
#116
#117
#118
#119
#120
#121
#122
#123
#124
#125
#126
#127
#128
#129
#130
#131
#132
#133
#134
#135
#136
#137
#138
#139
#140
#141
#142
#143
#144
#145
#146
#147
#148
#149
#150


