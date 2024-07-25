class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25
    
    >>> odd_cards = [1, 2, 3, 4, 5]
    >>> mod_oh_even = Shuffle.modified_overhand(odd_cards, 2)
    >>> mod_oh_even
    [1, 2, 3, 4, 5]
    """     
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        half = 2

        if num == 0:
            return cards
        
        halfway = len(cards) // half
        top = cards[:halfway]

        if len(cards) % 2 == 0:
            amount_remove = num // half
            bottom = cards[halfway:]
            bottom_removed = bottom[:amount_remove]
            bottom_keep = bottom[amount_remove:]
            if num % 2 == 0:
                top_removed = top[-amount_remove:]
                top_keep = top[:-amount_remove]
            else:
                top_removed = top[-(amount_remove+1):]
                top_keep = top[:-(amount_remove+1)]
            cards = top_removed + bottom_removed + \
                top_keep + bottom_keep
        else:
            amount_remove = (num - 1) // half
            bottom = cards[halfway+1:]
            middle = [cards[halfway]]
            bottom_removed = bottom[:amount_remove]
            bottom_keep = bottom[amount_remove:]
            if num % 2 != 0:
                if num == 1:
                    top_removed = []
                    top_keep = top
                else:
                    top_removed = top[-amount_remove:]
                    top_keep = top[:-amount_remove]
            else:
                top_removed = top[-(amount_remove+1):]
                top_keep = top[:-(amount_remove+1)]
            cards = top_removed + middle+ bottom_removed + \
                top_keep + bottom_keep

        return Shuffle.modified_overhand(cards, num-1)
                
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        
        if len(cards) == 0:
            return cards
        elif len(cards) % 2 == 0:
            return [cards[-1]] + Shuffle.mongean(cards[:-1])
        elif len(cards) % 2 != 0:
            return Shuffle.mongean(cards[:-1]) + [cards[-1]]
