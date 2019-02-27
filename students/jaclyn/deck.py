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

    def __init__(self, number: int=1):
        """
        Initialize the deck

        Args:
            number: the number of 52-card decks to create

        Returns:
            deck object
        """
        self._cards = [Card(rank, suit)
                       for rank in Card.ranks
                       for suit in Card.suits
                       for _ in range(number)] # _ value isn't used, just a counter
        # could also not use the 3rd loop and use this instead:
        # self._cards *= number

    def __len__(self) -> int:
        """ Returns length of deck """
        return len(self._cards)

    def __getitem__(self, index: int) -> Card:
        """ Acts like a list """
        return self._cards[index]

    def shuffle(self) -> None:
        """ Shuffle the deck """
        random.shuffle(self._cards)

    def deal(self) -> Card:
        """ Return a single Card from the top of the deck """
        return self._cards.pop()
