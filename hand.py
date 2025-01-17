from card import Card
from balatro import Balatro

class HandToPlay(Balatro):
    def __init__(self, cards: list[Card], cards_will_activate: list[bool],
                constainsHighCard      = True,
                constainsPair          = False,
                constainsTwoPair      = False,
                constainsThreeOfAKind  = False,
                constainsStraight      = False,
                constainsFlush         = False,
                constainsFullHouse     = False,
                constainsFourOfAKind   = False,
                constainsStraightFlush = False,
                constainsFiveOfAKind   = False,
                constainsFlushHouse    = False,
                constainsFlushFive     = False,
                ):
        self.cards = cards

        self.constainsHighCard      = constainsHighCard
        self.constainsPair          = constainsPair
        self.constainsTwoPair      = constainsTwoPair
        self.constainsThreeOfAKind  = constainsThreeOfAKind
        self.constainsStraight      = constainsStraight
        self.constainsFlush         = constainsFlush
        self.constainsFullHouse     = constainsFullHouse
        self.constainsFourOfAKind   = constainsFourOfAKind
        self.constainsStraightFlush = constainsStraightFlush
        self.constainsFiveOfAKind   = constainsFiveOfAKind
        self.constainsFlushHouse    = constainsFlushHouse
        self.constainsFlushFive     = constainsFlushFive
        self.cards_will_activate    = cards_will_activate


    def playingHandSize(self):
        return len(self.cards)

    def trigger_playing_hand(self):
        for i in range(self.playingHandSize()):
            if self.cards_will_activate[i]:
                self.cards[i].trigger_on_hand()

    def card_that_will_score(self):
        res = []
        for i in range(self.playingHandSize()):
            if self.cards_will_activate[i]:
                res.append(self.cards[i])
        return res

    #def score_from_hand_type(self):
    #    if self.constainsFlushFive():
    #        self.score_flush_five()
    #    elif self.constainsFlushHouse:
    #        self.score_constainsFlushFive()

    #def score_flush_five(self):
    #    self.scoreboard.add_chips(160 + 50*level_flush_five)

class HeldInHand(Balatro):
    def __init__(self, cards: list[Card]):
        self.cards = cards