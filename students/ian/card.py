"""
This module contains a simple class which represents a single playing
card.  It exists (rather than just using a named tuple) so that the
card can be aware of its own point value, and have a high-quality str()
representation.
"""

class Card():
    """ A simple class representing a single playing card; barely
    qualifies to be a class on its own """
    values = {str(num): num for num in range(2, 11)}
    values.update({'J': 10, 'Q': 10, 'K': 10, 'A': 1})

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.points = self.values[self.rank]

    def __repr__(self):
        return 'Card("{rank}", "{suit}")'.format(rank=self.rank, suit=self.suit)

    def __str__(self):
        return '{rank} of {suit}'.format(rank=self.rank, suit=self.suit.title())

    #def __eq__(self, other):
        #return self.value() == other.value()
