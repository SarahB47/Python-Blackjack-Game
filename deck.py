from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
     
    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, spades), (Q, spades), (10, spades), (7, hearts), (5, hearts)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, spades)
    """

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        suits = ['spades', 'hearts','diamonds', 'clubs']
        
        self.cards = [Card(r, s) for r in ranks for s in suits]


    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        assert isinstance(shuffle_and_count, dict)

        if 'modified_overhand' in shuffle_and_count:
            self.cards = Shuffle.modified_overhand(self.cards, \
                shuffle_and_count['modified_overhand'])

        if 'mongean' in shuffle_and_count:
            number_mongean = shuffle_and_count['mongean']
            while number_mongean > 0:
                self.cards = Shuffle.mongean(self.cards)
                number_mongean -= 1
            

    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        assert isinstance(hand, PlayerHand) or isinstance(hand, DealerHand)
        
        hand.add_card(self.get_cards()[0])
        self.cards.remove(self.get_cards()[0])

    def get_cards(self):
        return self.cards
