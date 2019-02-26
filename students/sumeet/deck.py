"""
This module defines a class that represents a deck of cards.  This class
exists to improve on a List by offering a built-in shuffle() method,
and a built-in deal() method, as well as being able to initialize itself
to a standard 52-card deck.
"""

# pylint: disable=fixme

import random
from card import Card

class Deck():
    """
    A deck of cards
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['clubs', 'diamonds', 'hearts', 'spades']


    def __init__(self, number: int = 1):
        """
        Initialize the deck

        Args:
            number: the number of 52-card decks to create

        Returns:
            Deck object
        """
        self._cards = [Card(rank, suit)
                       for rank in self.ranks
                       for suit in self.suits]
        self._cards *= number

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, index: int) -> Card:
        return self._cards[index]

    def shuffle(self) -> None:
        """ Shuffle the deck """
        random.shuffle(self._cards)

    def deal(self) -> Card:
        """ Return a single Card from the top of the deck """
        return self._cards.pop()
