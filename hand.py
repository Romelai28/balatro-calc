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

    def trigger_playing_hand(self):
        """Triggea todas las veces necesarias las cartas que se van a activar"""
        for i in range(self.playingHandSize()):
            if self.cards_will_activate[i]:
                self.trigger_on_hand(self.cards[i])

    def trigger_on_hand(self, card: Card):
        """Trigguea todas las veces necesaria la carta pasada por argumento"""
        for _ in range(card.number_of_triggers):
            card.trigger_one_time_on_hand()

    
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