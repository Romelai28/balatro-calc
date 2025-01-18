from jokers import JokersClass

class JokerToPlay:
    
    def __init__(self, jokers_to_play: list[JokersClass]):
        self.jokers_to_play = jokers_to_play

    def trigger_joker_editions_and_independents_jokers(self):
        for joker in self.jokers_to_play:
            joker.trigger_foil_and_holographic_bonus()
            joker.trigger_independent()
            # falta el baseball card
            joker.trigger_polychrome_bonus()

    def bind_on_score(self):
        for joker in self.jokers_to_play:
            joker.bind_on_score()

    def add_retriggers(self):
        for joker in self.jokers_to_play:
            joker.add_retriggers()