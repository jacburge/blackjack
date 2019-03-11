"""
This module contains a simple class which represents a single playing
card.  It exists (rather than just using a named tuple) so that the
card can be aware of its own point value, and have a high-quality str()
representation.
"""
# pylint: disable=too-few-public-methods

class Card():
    """ A simple class representing a single playing card; barely
    qualifies to be a class on its own """
    values = {str(num): num for num in range(2, 11)}
    values.update({'J': 10, 'Q': 10, 'K': 10, 'A': 1}) # A is a special case
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    combined = [(rank, suit)
                for suit in ['clubs','diamonds','hearts','spades']
                for rank in [str(n) for n in range(2, 11)] + list('JQKA')]

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.points = self.values[self.rank]

    def __repr__(self):
        return 'Card("{rank}", "{suit}")'.format(rank=self.rank, suit=self.suit)

    def __str__(self):
        return '{rank} of {suit}'.format(rank=self.rank, suit=self.suit.title())

    def __lt__(self, other):
        """
        Less than, this card is less than another card if value is less than the second
        """
        # return self.combined.index((self.rank, self.suit)) < self.combined.index((other.rank, other.suit))
        if self.suit == other.suit:
            return self.ranks.index(self.rank) < self.ranks.index(other.rank)
        else:
            return self.suits.index(self.suit) < self.suits.index(other.suit)
