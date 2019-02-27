"""
This module contains a simple class which represents a single playing
card.  It exists (rather than just using a named tuple) so that the
card can be aware of its own point value, and have a high-quality str()
representation.
"""

class Card():
    """ A simple class representing a single playing card; barely
    qualifies to be a class on its own """
    point_values = {str(num): num for num in range(2, 11)}
    point_values.update({'J': 10, 'Q': 10, 'K': 10}) # A is a special case
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['clubs', 'diamonds', 'hearts', 'spades']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return 'Card("{rank}", "{suit}")'.format(rank=self.rank, suit=self.suit)

    def __str__(self):
        return '{rank} of {suit}'.format(rank=self.rank, suit=self.suit.title())

    def __lt__(self, other) -> bool:
        return self.suits.index(self.suit) < self.suits.index(other.suit) \
                    or (self.suits.index(self.suit) == self.suits.index(other.suit)
                        and self.ranks.index(self.rank) < self.ranks.index(other.rank))

    @property
    def points(self) -> int:
        """ Return the point value of a card """
        if self.rank == 'A':
            return 1
        return self.point_values[self.rank]
