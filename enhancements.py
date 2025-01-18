from score import Score

class Enhancement:
    def __init__(self, scoreboard: Score):
        self.scoreboard = scoreboard

    def trigger_bonus_bonus(self):
        pass

    def isWildCard(self):
        return False

    def trigger_glass_bonus(self):
        pass

    def trigger_steel_bonus(self):
        pass

    def isStoneCard(self):
        return False


class BaseCard(Enhancement):
    pass


class BonusCard(Enhancement):
    def trigger_bonus_bonus(self):
        self.scoreboard.add_chips(30)


class MultCard(Enhancement):
    def trigger_mult_bonus(self):
        self.scoreboard.add_mult(4)


class WildCard(Enhancement):
    def isWildCard(self):
        return True


class GlassCard(Enhancement):
    def trigger_glass_bonus(self):
        self.scoreboard.times_mult(2)


class SteelCard(Enhancement):
    def trigger_steel_bonus(self):
        self.scoreboard.times_mult(1.5)


class StoneCard(Enhancement):
    # Card always scores
    def isStoneCard(self):
        return True


class GoldCard(Enhancement):
    pass


class LuckyCard(Enhancement):
    pass