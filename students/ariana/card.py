"""
This module contains a simple class which represents a single playing
card.  It exists (rather than just using a named tuple) so that the
card can be aware of its own point value, and have a high-quality str()
representation.
"""
# pylint: disable=fixme

class Card():
    """ A simple class representing a single playing card; barely
    qualifies to be a class on its own """
    values = {str(num): num for num in range(2, 11)}
    values.update({'J': 10, 'Q': 10, 'K': 10}) # A is a special case

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return 'Card("{rank}", "{suit}")'.format(rank=self.rank, suit=self.suit)

    def __str__(self):
        return '{rank} of {suit}'.format(rank=self.rank, suit=self.suit.title())

    # def __eq__(self, other):
    #     return self.value() == other.value()

    def value(self: object) -> int:
        """ Return the point value of a card """
        if self.rank == 'A':
            return 1
        return self.values[self.rank]
