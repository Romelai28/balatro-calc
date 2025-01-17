class Balatro:
    def __init__(self, hand_to_play, held_in_hand, jokers_to_play, scoreboard):
        self.hand_to_play = hand_to_play
        self.held_in_hand = held_in_hand
        self.jokers_to_play = jokers_to_play
        self.scoreboard = scoreboard

    def played_cards_scoring(self):
        """ Puntúa las cartas jugadas y aplica el multiplicador """

        # Fase 0: Puntaje del tipo de la mano.

        # Fase 2.5: Blindeo el comportamiento extra que le dan los jokers a las cartas. (on_score y on_held) [SOLO BLINDEA, NO HACE NADA]
        self.jokers_to_play.bind_on_score()


        # Fase 3:
        self.hand_to_play.trigger_playing_hand()

        # Fase 5: Joker editions and independent jokers
        self.jokers_to_play.trigger_joker_editions_and_independents_jokers()