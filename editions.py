from score import Score

class Editions:
    def __init__(self, scoreboard: Score):
        self.scoreboard = scoreboard

    def trigger_foil_or_holographic_bonus(self):
        pass

    def trigger_polychrome_bonus(self):
        pass

    def trigger_any_edition(self):
        self.trigger_foil_or_holographic_bonus()
        self.trigger_polychrome_bonus()

class BaseEdition(Editions):
    pass

class FoilEdition(Editions):
    def trigger_foil_or_holographic_bonus(self):
        self.scoreboard.add_chips(50)

class HolographicEdition(Editions):
    def trigger_foil_or_holographic_bonus(self):
        self.scoreboard.add_mult(10)

class PolychromeEdition(Editions):
    def trigger_polychrome_bonus(self):
        self.scoreboard.times_mult(1.5)
