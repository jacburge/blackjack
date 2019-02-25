import sys
sys.path.insert(0, '..')

import unittest
from deck import Deck
from player import Player
import game
from card import Card

from collections import Counter
import random

class TestGame(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.p1 = Player('Bob')

    def test_deal_cards(self):
        num_cards = 2
        game.deal_cards(self.deck, self.p1, num_cards)
        self.assertEqual(num_cards, len(self.p1.visible_cards()))

    def test_dealt_cards_are_different(self):
        num_cards = 10
        dealt_cards = set([self.deck.deal() for _ in range(num_cards)])
        self.assertEqual(num_cards, len(dealt_cards))

    def test_dealt_cards_from_multiple_decks_are_varied(self):
        num_cards = 52
        num_decks = 2
        test_decks = []
        for _ in range(num_decks):
            d = Deck()
            d.shuffle
            test_decks.append(d)
        dealt_cards = [random.choice(test_decks).deal() for _ in range(num_cards)]

        # Counter() will create a list of tuples of the counts of all cards.
        c = Counter(dealt_cards)

        # most_common(n) returns a list of tuples of the n most common elements and their
        # counts. E.g., [(val, 5), (val2, 3) ...]
        self.assertLessEqual(c.most_common(1)[0][1], num_decks)

    def test_basic_score_determination(self):
        self.p1.add_card(Card('5', 'hearts'))
        self.p1.add_card(Card('A', 'diamonds'))
        self.assertEqual(16, game.get_score(self.p1))

    def test_blackjack_score_determination(self):
        self.p1.add_card(Card('10', 'hearts'))
        self.p1.add_card(Card('A', 'diamonds'))
        self.assertEqual(21, game.get_score(self.p1))

    def test_harder_score_determination(self):
        self.p1.add_card(Card('A', 'diamonds'))
        self.p1.add_card(Card('A', 'clubs'))
        self.p1.add_card(Card('10', 'hearts'))
        self.p1.add_card(Card('7', 'diamonds'))
        self.assertEqual(19, game.get_score(self.p1))

    def test_other_score_determination(self):
        self.p1.add_card(Card('4', 'hearts'))
        self.p1.add_card(Card('7', 'diamonds'))
        self.p1.add_card(Card('A', 'clubs'))
        self.assertEqual(12, game.get_score(self.p1))

    def test_ace_score_over_21(self):
        self.p1.add_card(Card('10', 'hearts'))
        self.p1.add_card(Card('10', 'diamonds'))
        self.p1.add_card(Card('A', 'clubs'))
        self.p1.add_card(Card('A', 'clubs'))
        self.assertEqual(22, game.get_score(self.p1))

    def test_one_ace_11_and_one_1(self):
        self.p1.add_card(Card('9', 'hearts'))
        self.p1.add_card(Card('A', 'clubs'))
        self.p1.add_card(Card('A', 'clubs'))
        self.assertEqual(21, game.get_score(self.p1))


if __name__ == '__main__':
    unittest.main()
