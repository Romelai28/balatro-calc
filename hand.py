from card import Card


class HandToPlay():
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


    def played_cards_scoring(self):
        """Le dice que triggee todas las veces necesarias a las cartas que se van a activar"""
        for scoring_card in self.card_that_will_score():
            scoring_card.trigger_on_hand()

    
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

class HeldInHand():
    def __init__(self, cards: list[Card]):
        self.cards = cards

    def all_spades_or_clubs(self):
        for card in self.cards:
            if not (card.isSpadeSuit() or card.isClubSuit()):
                return False
        return True
    

    def held_in_hand_habilities(self):
        for card in self.cards:
            card.trigger_on_held()