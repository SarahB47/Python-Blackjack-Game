class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    True

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        card_rank_start = 2
        card_rank_end = 11

        assert isinstance(rank, str) or isinstance(rank, int)
        assert rank in range(card_rank_start, card_rank_end) or \
            rank in ['A', 'J', 'Q', 'K']
        self.rank = rank

        assert isinstance(suit, str)
        assert suit in ['hearts', 'spades', 'clubs', 'diamonds']
        self.suit = suit

        assert isinstance(visible, bool)
        self.visible = visible


    def __lt__(self, other_card):
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        suits = ['spades', 'hearts','diamonds', 'clubs']
        if self.get_rank() == other_card.get_rank():
            return suits.index(self.get_suit()) < \
                suits.index(other_card.get_suit())

        else:
            return ranks.index(self.get_rank()) < \
                ranks.index(other_card.get_rank())


    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        
        if self.suit == 'hearts':
            symbol = '♥'
        elif self.suit == 'spades':
            symbol = '♠'
        elif self.suit == 'clubs':
            symbol = '♣'
        else:
            symbol = '♦'
        
        if self.visible:
            card = '____\n|{0}  |\n| {1} |\n|__{0}|'\
                .format(self.get_rank(), symbol)
        else:
            card = '____\n|?  |\n| ? |\n|__?|'

        return card

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """
        if self.visible:
            return '({}, {})'.format(self.get_rank(), self.get_suit())
        else:
            return '(?, ?)'

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit

    def set_visible(self, visible):

        assert isinstance(visible, bool)
        self.visible = visible
