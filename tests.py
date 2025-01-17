import unittest
from score import Score
from card import Card
from hand import HandToPlay
from hand import HeldInHand
from joker_to_play import JokerToPlay
from jokers import *
from balatro import Balatro
from editions import *

class TestHandMethods(unittest.TestCase):
    
    def test_hand_contains_pair(self):
        print("test1:")
        scoreboard = Score()

        # Crear cartas
        card1 = Card(suit='Corazones', rank='A', scoreboard=scoreboard)
        card2 = Card(suit='Diamantes', rank='K', scoreboard=scoreboard)
        card3 = Card(suit='Tréboles', rank='K', scoreboard=scoreboard)
        card4 = Card(suit='Espadas', rank='J', scoreboard=scoreboard)
        
        # Crear una mano con las cartas
        hand_to_play = HandToPlay(cards=[card1, card2, card3, card4], cards_will_activate=[False, True, True, False], constainsPair=True)
        held_in_hand = HeldInHand(cards=[])

        jokers_to_play = JokerToPlay(jokers_to_play=[
                                                    JollyJoker(hand_to_play=hand_to_play, scoreboard=scoreboard, edition=BaseEdition(scoreboard))
                                                    ]
                                    )

        balatro = Balatro(hand_to_play=hand_to_play,
                          held_in_hand=held_in_hand,
                          jokers_to_play=jokers_to_play,
                          scoreboard=scoreboard)


        balatro.played_cards_scoring()
        # Probar si la mano contiene un par
        print(f"chips: {scoreboard.chips}")
        print(f"mult: {scoreboard.mult}")
        print(f"final score: {scoreboard.final_score()}")
        #self.assertTrue(hand.checkHandContainsPair())  # Debería devolver True porque hay un par de 'K'

    def test2(self):
        print("test2:")
        scoreboard = Score()

        # Crear cartas
        card1 = Card(suit='Diamond', rank='A', scoreboard=scoreboard)
        card2 = Card(suit='Diamond', rank='K', scoreboard=scoreboard)
        card3 = Card(suit='Diamond', rank='K', scoreboard=scoreboard)
        card4 = Card(suit='Espadas', rank='J', scoreboard=scoreboard)
        
        # Crear una mano con las cartas
        hand_to_play = HandToPlay(cards=[card1, card2, card3, card4], cards_will_activate=[False, True, True, False], constainsPair=True)
        held_in_hand = HeldInHand(cards=[])

        jokers_to_play = JokerToPlay(jokers_to_play=[
                                                    JollyJoker(hand_to_play=hand_to_play, scoreboard=scoreboard, edition=BaseEdition(scoreboard)),
                                                    GreedyJoker(hand_to_play=hand_to_play, scoreboard=scoreboard, edition=BaseEdition(scoreboard))
                                                    ]
                                    )

        balatro = Balatro(hand_to_play=hand_to_play,
                          held_in_hand=held_in_hand,
                          jokers_to_play=jokers_to_play,
                          scoreboard=scoreboard)


        balatro.played_cards_scoring()
        # Probar si la mano contiene un par
        print(f"chips: {scoreboard.chips}")
        print(f"mult: {scoreboard.mult}")
        print(f"final score: {scoreboard.final_score()}")
        #self.assertTrue(hand.checkHandContainsPair())  # Debería devolver True porque hay un par de 'K'

if __name__ == '__main__':
    unittest.main()
