from hand import HandToPlay
from hand import HeldInHand
from score import Score
from editions import *
from game_info import GameInfo

class JokersClass:
    def __init__(self, hand_to_play: HandToPlay, held_in_hand: HeldInHand, game_info: GameInfo, scoreboard: Score, edition: Editions = None):
        self.hand_to_play = hand_to_play
        self.held_in_hand = held_in_hand
        self.scoreboard = scoreboard
        if edition is None:
            self.edition = BaseEdition(self.scoreboard)
        else:
            self.edition = edition
        self.game_info = game_info

    def trigger_foil_and_holographic_bonus(self):
        self.edition.trigger_foil_and_holographic_bonus()

    def trigger_polychrome_bonus(self):
        self.edition.trigger_polychrome_bonus()
    
    def on_played(self):
        pass

    def bind_on_score(self):
        pass
    
    def bind_on_held(self):
        pass
    
    def trigger_independent(self):
        pass

    def add_retriggers(self):
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

                card.trigger_on_scored_jokers = decorator(card.trigger_on_scored_jokers)
    

    def bind_on_held_generic(self, condition, codigo_a_agregar):
        for card in self.held_in_hand.cards:
            if condition(card):

                def decorator(old_method_trigger_on_held):
                    def wrapper():
                        # Lineas antes
                        old_method_trigger_on_held()
                        # Lineas dps
                        codigo_a_agregar()
                    return wrapper

                card.trigger_on_held_jokers = decorator(card.trigger_on_held_jokers)


## TODO: eliminar codigo repetido, me falta una abstracción parametrizedjoker class, apply_value metodo.

class Parameterized_ChipsJoker(JokersClass):
    def __init__(self, hand_to_play, held_in_hand, game_info, scoreboard, edition = None, current_chips_value = 0):
        super().__init__(hand_to_play, held_in_hand, game_info, scoreboard, edition)
        self.current_chips_value = current_chips_value

    def trigger_independent(self):
        self.scoreboard.add_chips(self.current_chips_value)


class Parameterized_MultJoker(JokersClass):
    def __init__(self, hand_to_play, held_in_hand, game_info, scoreboard, edition = None, current_mult_value = 0):
        super().__init__(hand_to_play, held_in_hand, game_info, scoreboard, edition)
        self.current_mult_value = current_mult_value

    def trigger_independent(self):
        self.scoreboard.add_mult(self.current_mult_value)


class Parameterized_XMultJoker(JokersClass):
    def __init__(self, hand_to_play, held_in_hand, game_info, scoreboard, edition = None, current_xmult_value = 1):
        super().__init__(hand_to_play, held_in_hand, game_info, scoreboard, edition)
        self.current_xmult_value = current_xmult_value

    def trigger_independent(self):
        self.scoreboard.times_mult(self.current_xmult_value)


# 1
class Joker(JokersClass):
    """+4 mult"""
    def trigger_independent(self):
        self.scoreboard.add_mult(4)


# 2
class GreedyJoker(JokersClass):
    """Played cards with Diamond suit give +3 Mult when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isDiamondSuit,
                                   lambda: self.scoreboard.add_mult(3))


# 3
class LustyJoker(JokersClass):
    """Played cards with Heart suit give +3 Mult when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isHeartSuit,
                                   lambda: self.scoreboard.add_mult(3))


# 4
class WrathfulJoker(JokersClass):
    """Played cards with Spade suit give +3 Mult when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isSpadeSuit,
                                   lambda: self.scoreboard.add_mult(3))


# 5
class GluttonousJoker(JokersClass):
    """Played cards with Club suit give +3 Mult when scored """
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isClubSuit,
                                   lambda: self.scoreboard.add_mult(3))


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


#17
class JokerStencil(Parameterized_XMultJoker):
    """X1 Mult for each empty Joker slot. Joker Stencil included"""
    # SUPERCLASS RESPONSABILITY
    pass


#18


#19
class Mime(JokersClass):
    def add_retriggers(self):
        for card in self.held_in_hand.cards:
            card.increment_trigger_count_on_held

#20
class CreditCard(JokersClass):
    """Go up to -$20 in debt"""
    pass


#21
class CeremonialDagger(Parameterized_MultJoker):
    """When Blind is selected, destroy Joker to the right and permanently add double its sell value to this Mult (Currently +0 Mult)"""
    # SUPERCLASS RESPONSABILITY
    pass


#22
class Banner(JokersClass):
    """+30 Chips for each remaining discard"""
    def trigger_independent(self):
        self.scoreboard.add_chips(30 * self.game_info.remaining_discards)


#23
class MysticSummit(JokersClass):
    """+15 Mult when 0 discards remaining"""
    def trigger_independent(self):
        if self.game_info.remaining_discards == 0:
            self.scoreboard.add_mult(15)


#24
class MarbleJoker(JokersClass):
    """Adds one Stone card to the deck when Blind is selected"""
    pass


#25


#26
#27

#28
class Dusk(JokersClass):
    """Retrigger all played cards in final hand of the round"""
    def add_retriggers(self):
        if self.game_info.isFinalHand():
            for card in self.hand_to_play.card_that_will_score():
                card.increment_trigger_count_on_hand()

#29


#30
class ChaosTheClown(JokersClass):
    """1 free Reroll per shop"""
    pass


#31
class Fibonacci(JokersClass):
    """Each played Ace, 2, 3, 5, or 8 gives +8 Mult when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isFibonacciRank,
                                   lambda: self.scoreboard.add_mult(8))


#32
class SteelJoker(Parameterized_XMultJoker):
    """Gives X0.2 Mult for each Steel Card in your full deck"""
    # SUPERCLASS RESPONSABILITY
    pass


#33
class ScaryFace(JokersClass):
    """"Played face cards give +30 Chips when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isFaceCard,
                                   lambda: self.scoreboard.add_chips(30))



#34


#35
class DelayedGratification(JokersClass):
    """Earn $2 per discard if no discards are used by end of the round"""
    pass


#36
class Hack(JokersClass):
    """Retrigger each played 2, 3, 4, or 5"""
    def add_retriggers(self):
        for card in self.hand_to_play.card_that_will_score():
            if card.is234or5Rank(): 
                card.increment_trigger_count_on_hand()


#37


#38
class GrosMichel(JokersClass):
    """+15 Mult. 1 in 6 chance this is destroyed at the end of round."""
    def trigger_independent(self):
        self.scoreboard.add_mult(15)


#39
class EvenSteven(JokersClass):
    """Played cards with even rank give +4 Mult when scored  (10, 8, 6, 4, 2)"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isEvenRank,
                                   lambda: self.scoreboard.add_mult(4)) 


#40
class OddTodd(JokersClass):
    """Played cards with odd rank give +31 Chips when scored (A, 9, 7, 5, 3)"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isOddRank,
                                   lambda: self.scoreboard.add_chips(31)) 


#41
class Scholar(JokersClass):
    """Played Aces give +20 Chips and +4 Mult when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isAceRank,
                                   lambda: (self.scoreboard.add_chips(20),
                                            self.scoreboard.add_mult(4)))

#42
#43
#44
#45


#46
class Egg(JokersClass):
    """Gains $3 of sell value at end of round"""
    pass


#47


#48
class Blackboard(JokersClass):
    """X3 Mult if all cards held in hand are Spade or Club"""
    def trigger_independent(self):
        if self.held_in_hand.all_spades_or_clubs():
            self.scoreboard.times_mult(3)


#49


#50
class IceCream(Parameterized_ChipsJoker):
    """+100 Chips. -5 Chips for every hand played"""
    # SUPERCLASS RESPONSABILITY (OJO ACORDATE DE PONER 100)
    pass


#51
#52
#53
#54


#55
class Constellation(Parameterized_XMultJoker):
    """This Joker gains X0.1 Mult every time a Planet card is used"""
    # SUPERCLASS RESPONSABILITY
    pass
        



#56



#57
class FacelessJoker(JokersClass):
    """Earn $5 if 3 or more face cards are discarded at the same time"""
    pass


#58
#59
#60


#61
class Cavendish(JokersClass):
    """X3 Mult. 1 in 1000 chance this card is destroyed at the end of round"""
    def trigger_independent(self):
        self.scoreboard.times_mult(3)


#62


#63
class RedCard(Parameterized_MultJoker):
    """This Joker gains +3 Mult when any Booster Pack is skipped"""
    # SUPERCLASS RESPONSABILITY
    pass


#64
class Madness(Parameterized_XMultJoker):
    """When Small Blind or Big Blind is selected, gain X0.5 Mult and destroy a random Joker"""
    # SUPERCLASS RESPONSABILITY
    pass

#65
#66


#67
class RiffRaff(JokersClass):
    """When Blind is selected, create 2 Common Jokers"""
    pass

#68
#69


#70
class Hologram(Parameterized_XMultJoker):
    ### OJO CUANDO IMPLEMENTE ADN Y TENGA ESTA CARTA JUNTO CON ADN ACTIVO.
    """This Joker gains X0.25 Mult every time a playing card is added to your deck"""    
    # SUPERCLASS RESPONSABILITY
    pass


#71
class Vagabond(JokersClass):
    """Create a Tarot card if hand is played with $4 or less"""
    pass


#72
class Baron(JokersClass):
    """Each King held in hand gives X1.5 Mult"""
    def bind_on_held(self):
        self.bind_on_held_generic(lambda card: card.isKingRank(),
                                  lambda: self.scoreboard.times_mult(1.5))

#73
class Cloud9(JokersClass):
    """Earn $1 for each 9 in your full deck at end of round"""
    pass


#74
class Rocket(JokersClass):
    """Earn $1 at end of round. Payout increases by $2 when Boss Blind is defeated"""
    pass


#75
#76
#77
#78


#79
class GiftCard(JokersClass):
    """Add $1 of sell value to every Joker and Consumable card at end of round"""
    pass


#80
class TurtleBean(JokersClass):
    """+5 hand size, reduces by 1 each round"""
    pass


#81
class Erosion(Parameterized_MultJoker):
    """+4 Mult for each card below [the deck's starting size] in your full deck"""
    # SUPERCLASS RESPONSABILITY
    pass


#82


#83
class MailInRebate(JokersClass):
    """Earn $5 for each discarded [rank], rank changes every round """
    pass


#84
class ToTheMoon(JokersClass):
    """Earn an extra $1 of interest for every $5 you have at end of round"""
    pass


#85


#86
class FortuneTeller(Parameterized_MultJoker):
    """+1 Mult per Tarot card used this run"""
    # SUPERCLASS RESPONSABILITY
    pass


#87
class Juggler(JokersClass):
    """+1 hand size"""
    pass


#88
class Drunkard(JokersClass):
    """+1 discard each round"""
    pass


#89
class StoneJoker(Parameterized_ChipsJoker):
    """Gives +25 Chips for each Stone Card in your full deck"""
    # SUPERCLASS RESPONSABILITY
    pass


#90
class GoldenJoker(JokersClass):
    """Earn $4 at end of round"""
    pass


#91
class LuckyCat(Parameterized_XMultJoker):
    """This Joker gains X0.25 Mult every time a Lucky card successfully triggers"""
    # SUPERCLASS RESPONSABILITY
    pass


#92
#93
class Bull(Parameterized_ChipsJoker):
    """+2 Chips for each $1 you have"""
    # SUPERCLASS RESPONSABILITY
    pass

#94
class DietCola(JokersClass):
    """Sell this card to create a free Double Tag"""
    pass


#95
class TradingCard(JokersClass):
    """If first discard of round has only 1 card, destroy it and earn $3"""
    pass


#96
class FlashCard(Parameterized_MultJoker):
    """This Joker gains +2 Mult per reroll in the shop"""
    # SUPERCLASS RESPONSABILITY
    pass


#97
class Popcorn(Parameterized_MultJoker):
    """+20 Mult. -4 Mult per round played """
    # SUPERCLASS RESPONSABILITY
    pass


#98
class SpareTrousers(Parameterized_MultJoker):
    """This Joker gains +2 Mult if played hand contains a Two Pair"""
    # SUPERCLASS RESPONSABILITY
    pass


#99


#100
class Ramen(Parameterized_XMultJoker):
    """X2 Mult, loses X0.01 Mult per card discarded"""
    # SUPERCLASS RESPONSABILITY
    pass


#101
class WalkieTalkie(Joker):
    """Each played 10 or 4 gives +10 Chips and +4 Mult when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.is4or10Rank(),
                                   lambda: (self.scoreboard.add_chips(10),
                                            self.scoreboard.add_mult(4)))


#102


#103
class Castle(Parameterized_ChipsJoker):
    """This Joker gains +3 Chips per discarded [suit] card, suit changes every round"""
    # SUPERCLASS RESPONSABILITY
    pass


#104
class SmileyFace(JokersClass):
    """Played face cards give +5 Mult when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isFaceCard,
                                   lambda: self.scoreboard.add_mult(5))


#105
class Campfire(Parameterized_XMultJoker):
    """This Joker gains X0.25 Mult for each card sold, resets when Boss Blind is defeated"""
    # SUPERCLASS RESPONSABILITY
    pass


#106
#107
#108


#109
class SockAndBuskin(JokersClass):
    def add_retriggers(self):
        for card in self.hand_to_play.card_that_will_score():
            if card.isFaceCard():
                card.increment_trigger_count_on_hand()


#110
class Swashbuckler(Parameterized_MultJoker):
    """Adds the sell value of all other owned Jokers to Mult"""
    # SUPERCLASS RESPONSABILITY
    pass


#111
class Troubadour(JokersClass):
    """+2 hand size, 1 hand per round"""
    pass


#112
class Certificate(JokersClass):
    """When round begins, add a random playing card with a random seal to your hand"""
    pass


#113

#114
class Throwback(Parameterized_XMultJoker):
    """X0.25 Mult for each Blind skipped this run"""
    # SUPERCLASS RESPONSABILITY
    pass


#115
class HangingChad(JokersClass):
    """Retrigger first played card used in scoring 2 additional times"""
    def add_retriggers(self):
        first_card = self.hand_to_play.card_that_will_score()[0]
        first_card.increment_trigger_count_on_hand()


#116
#117


#118
class Arrowhead(JokersClass):
    """Played cards with Spade suit give +50 Chips when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isSpadeSuit,
                                   lambda: self.scoreboard.add_chips(50))


#119
class OnyxAgate(JokersClass):
    """Played cards with Club suit icon Club suit give +7 Mult when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isClubSuit,
                                   lambda: self.scoreboard.add_mult(7))


#120
class GlassJoker(Parameterized_XMultJoker):
    """This Joker gains X0.75 Mult for every Glass Card that is destroyed"""
    # SUPERCLASS RESPONSABILITY
    pass


#121
class Showman(JokersClass):
    """Joker, Tarot, Planet, and Spectral cards may appear multiple times"""
    pass


#122
#123
#124


#125
class MerryAndy(JokersClass):
    """+3 discards each round, -1 hand size"""
    pass


#126
#127
#128
#129


#130
class HitTheRoad(Parameterized_XMultJoker):
    """This Joker gains X0.5 Mult for every Jack discarded this round"""
    # SUPERCLASS RESPONSABILITY
    pass


#131
class TheDuo(JokersClass):
    """X2 Mult if played hand contains a Pair"""
    def trigger_independent(self):
        if self.hand_to_play.constainsPair:
            self.scoreboard.times_mult(2)


#132
class TheTrio(JokersClass):
    """X3 Mult if played hand contains a Three of a Kind"""
    def trigger_independent(self):
        if self.hand_to_play.constainsThreeOfAKind:
            self.scoreboard.times_mult(3)


#133
class TheFamily(JokersClass):
    """X4 Mult if played hand contains a Four of a Kind"""
    def trigger_independent(self):
        if self.hand_to_play.constainsFourOfAKind:
            self.scoreboard.times_mult(4)


#134
class TheOrder(JokersClass):
    """X3 Mult if played hand contains a Straight"""
    def trigger_independent(self):
        if self.hand_to_play.constainsStraight:
            self.scoreboard.times_mult(3)


#135
class TheTribe(JokersClass):
    """X2 Mult if played hand contains a Flush"""
    def trigger_independent(self):
        if self.hand_to_play.constainsFlush:
            self.scoreboard.times_mult(2)


#136
class Stuntman(JokersClass):
    """+250 Chips, -2 hand size."""
    def trigger_independent(self):
        self.scoreboard.add_chips(250)


#137
class InvisibleJoker(JokersClass):
    """After 2 rounds, sell this card to Duplicate a random Joker"""
    pass


#138


#139
class Satellite(JokersClass):
    """Earn $1 at end of round per unique Planet card used this run"""
    pass


#140
class ShootTheMoon(JokersClass):
    """Each Queen held in hand gives +13 Mult"""
    def bind_on_held(self):
        self.bind_on_held_generic(lambda card: card.isQueenRank(),
                                  lambda: self.scoreboard.add_mult(13))


#141


#142
class Cartomancer(JokersClass):
    """Create a Tarot card when Blind is selected"""
    pass


#143
class Astronomer(JokersClass):
    """All Planet cards and Celestial Packs in the shop are free"""
    pass


#144
class BurntJoker(JokersClass):
    """Upgrade the level of the first discarded poker hand each round"""
    pass


#145
class Bootstraps(Parameterized_MultJoker):
    """+2 Mult for every $5 you have"""
    # SUPERCLASS RESPONSABILITY
    pass


#146
class Canio(Parameterized_XMultJoker):
    """This Joker gains X1 Mult when a face card is destroyed """
    # SUPERCLASS RESPONSABILITY
    pass


#147
class Triboulet(JokersClass):
    """Played Kings and Queens each give X2 Mult when scored"""
    def bind_on_score(self):
        self.bind_on_score_generic(lambda card: card.isKingRank() or card.isQueenRank(),
                                   lambda: self.scoreboard.times_mult(2))    


#148
class Yorick(Parameterized_XMultJoker):
    """This Joker gains X1 Mult every 23 [23] cards discarded"""
    # SUPERCLASS RESPONSABILITY
    pass


#149
#150
