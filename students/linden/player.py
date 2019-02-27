"""
This module contains a basic Player class so each player can keep track
of its own state.
"""

from typing import List

from card import Card


class Player():
    """ The person playing the game. """

    def __init__(self, name: str, is_dealer: bool = False):
        self.name = name
        self.is_dealer = is_dealer
        self._faceup_cards: List = []
        self._facedown_card = None

    def add_card(self, card: Card) -> None:
        """ Add a card to the player's hand.  This will correctly hide
        the first card the player gets, if the player is a dealer. """
        if self.is_dealer and not self._facedown_card:
            self._facedown_card = card
        else:
            self._faceup_cards.append(card)

    @property
    def visible_cards(self) -> list:
        """ Return a list of the player's visible cards """
        return self._faceup_cards

    @property
    def all_cards(self) -> list:
        """ Return a list of all the player's cards, whether visible or
        not. """
        cards = []
        cards.extend(self._faceup_cards)
        if self._facedown_card:
            cards.append(self._facedown_card)
        return cards
