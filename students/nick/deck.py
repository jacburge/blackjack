"""
This module defines a class that represents a deck of cards.  This class
exists to improve on a List by offering a built-in shuffle() method,
and a built-in deal() method, as well as being able to initialize itself
to a standard 52-card deck.
"""

import random
from card import Card

class Deck():
    """
    A deck of cards
    """

    def __init__(self, number: int = 1):
        self._cards = [Card(rank, suit)
                       for rank in Card.ranks
                       for suit in Card.suits
                       for num in range(number)]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, index: int) -> Card:
        return self._cards[index]

    def shuffle(self) -> None:
        """ Shuffle the deck """
        random.shuffle(self._cards)

    def deal(self) -> Card:
        """ Return a single Card from the top of the deck
            Bug #2253: Use .pop() instead of 'peek' (_cards[0]) """
        return self._cards.pop()
