import random
import pickle

ranks_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def card_ranks(cards):
    """Return the card ranks in reverse order
    without the suit"""
    ranks = []
    for card in cards:
        card = card[:-1]
        ranks.append(ranks_dict[card])
    ranks.sort(reverse=True)
    return ranks

def kind(n, ranks):
    """ Return the n of a kind
    Return None if not found"""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None

def two_pair(ranks):
    """Return True if it is two pair, False otherwise"""
    pair = kind(2, ranks)
    another_pair = kind(2,list(reversed(ranks)))
    if pair and another_pair != pair:
        return True 
    return False

def card_type(hand):
    ranks = card_ranks(hand)
    if kind(4, ranks):
        return 5
    elif kind(3, ranks) and kind(2, ranks):
        return 4
    elif kind(3, ranks):
        return 3
    elif two_pair(ranks):
        return 2
    elif kind(2, ranks):
        return 1
    else:
        return 0


def test():
    "Test cases for poker game"
    assert(card_type(['2♦', '3♣', 'K♥', '5♠', '7♣']) == 0)
    assert(card_type(['2♦', 'K♣', 'K♥', '3♠', '7♣']) == 1)
    assert(card_type(['2♦', '2♣', '3♥', '3♠', '7♣']) == 2)
    assert(card_type(['2♦', '3♣', '3♥', '3♠', '7♣']) == 3)
    assert(card_type(['2♦', '3♣', '3♥', '3♠', '2♣']) == 4)
    assert(card_type(['2♦', '3♣', '3♥', '3♠', '3♣']) == 5)
    return 'test pass'

if __name__ == "__main__":
    print(test())
    infile = open("DeckOfCardsList.dat", 'rb')
    deckOfCards = pickle.load(infile)
    infile.close()
    pokerHand = random.sample(deckOfCards, 5)
    print(pokerHand)
    print(card_type(pokerHand))
