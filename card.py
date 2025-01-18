from score import Score

class Card:
    scores = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9, 
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11
    }

    def __init__(self, suit: str, rank: str, scoreboard: Score):
        self.suit = suit
        self.rank = rank
        self.scoreboard = scoreboard  # Pasamos la instancia de Balatro para acceder a los chips

    def isDiamondSuit(self):
        return self.suit == "Diamond"

    def isHeartSuit(self):
        return self.suit == "Heart"

    def isSpadeSuit(self):
        return self.suit == "Spade"

    def isClubSuit(self):
        return self.suit == "Club"

    def isFibonacciRank(self):
        return self.rank in ['2', '3', '5', '8', 'A']
    
    def isFaceCard(self):
        return self.rank in ['J', 'Q', 'K']
    
    def isEvenRank(self):
        return self.rank in ['2', '4', '6', '8', '10']
    
    def isOddRank(self):
        return self.rank in ['A', '3', '5', '7', '9']
    
    def isAceRank(self):
        return self.rank == 'A'

    def is4or10Rank(self):
        return self.rank == '4' or self.rank == '10'

    def get_base_score(self):
        """ Devuelve el puntaje de la carta basado en su rango """
        return self.scores[self.rank]

    def trigger_base_effect(self):
        self.scoreboard.add_chips(self.get_base_score())
        #  Bonus chips van a caer aca también en un futuro

    def trigger_on_hand(self):
        """ Llama al método de agregar chips a la instancia de Balatro """
        # Va a tener 3 fases:
        # Base effect (chips)
        self.trigger_base_effect()
        # Card modifiers
        # On scored jokers.
        # Esto se repite la cantidad de triggers, (esto va por afuera, se va a llamar varias veces a esta funcion)