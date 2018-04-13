import random
import pickle

class Card:
    SUITS = {'♣': 1, '♦': 2, '♥': 3, '♠': 4}
    RANKS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
'9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, cardInfo):
        self.rank = self.RANKS[cardInfo[:-1]]
        self.suit = self.SUITS[cardInfo[-1]]

    def __toString__(self):
        text = ""
        if self.rank < 0:
            return "Joker";
        elif self.rank == 11:
            text = "J"
        elif self.rank == 12:
            text = "Q"
        elif self.rank == 13:
            text = "K"
        elif self.rank == 14:
            text = "A"
        else:
            text = str(self.rank)
        if self.suit == 0: #D-Diamonds
            text += "♦"
        elif self.suit == 1: #H-Hearts
            text += "♥"
        elif self.suit == 2: #S-Spade
            text += "♠"
        else: #C-Clubs
            text += "♣"
        return text

class Hand:
    CATEGORIES = {0: "Ranks-all-different",
                  1: "One pair",
                  2: "Two pairs",
                  3: "Three of a kind",
                  4: "Full house",
                  5: "Four of a kind"}

    def __init__(self, cards):
        self.cards = cards
        self.ranks = []

    def card_ranks(self):
        """Return the card ranks in reverse order
        without the suit"""
        for card in self.cards:
            self.ranks.append(card.rank)
        self.ranks.sort(reverse=True)

    def kind(self, n, ranks):
        """ Return the n of a kind
        Return None if not found"""
        for r in ranks:
            if ranks.count(r) == n:
                return r
        return None

    def two_pair(self):
        """Return True if it is two pair, False otherwise"""
        pair = self.kind(2, self.ranks)
        another_pair =self.kind(2,list(reversed(self.ranks)))
        if pair and another_pair != pair:
            return True
        return False

    def card_type(self):
        self.card_ranks()
        if self.kind(4, self.ranks):
            return 5
        elif self.kind(3, self.ranks) and self.kind(2, self.ranks):
            return 4
        elif self.kind(3, self.ranks):
            return 3
        elif self.two_pair():
            return 2
        elif self.kind(2, self.ranks):
            return 1
        else:
            return 0
        
    def category_str (self,category):
        return self.CATEGORIES[category]

def test():
    "Test cases for poker game"
    assert(Hand([Card('2♦'), Card('3♣'), Card('K♥'), Card('5♠'), Card('7♣')]).card_type() == 0)
    assert(Hand([Card('2♦'), Card('K♣'), Card('K♥'), Card('3♠'), Card('7♣')]).card_type() == 1)
    assert(Hand([Card('2♦'), Card('2♣'), Card('3♥'), Card('3♠'), Card('7♣')]).card_type() == 2)
    assert(Hand([Card('2♦'), Card('3♣'), Card('3♥'), Card('3♠'), Card('7♣')]).card_type() == 3)
    assert(Hand([Card('2♦'), Card('3♣'), Card('3♥'), Card('3♠'), Card('2♣')]).card_type() == 4)
    assert(Hand([Card('2♦'), Card('3♣'), Card('3♥'), Card('3♠'), Card('3♣')]).card_type() == 5)
    return '\ntest pass\n'

if __name__ == "__main__":
    print(test())
    infile = open("DeckOfCardsList.dat", 'rb')
    deckOfCards = pickle.load(infile)
    infile.close()
    pokerHand = random.sample(deckOfCards, 5)
    print(pokerHand)
    hand = Hand([Card(hand) for hand in pokerHand])
    category = hand.card_type()
    print("\nThe above hand's category: " + hand.category_str(category))

