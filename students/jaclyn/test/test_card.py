""" run tests on Card functionality """

import unittest
import sys
from parameterized import parameterized

sys.path.insert(0, '..')

from card import Card # pylint: disable=wrong-import-position

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card_2s = Card('2', 'spades')
        self.card_kh = Card('K', 'hearts')
        self.card_10d = Card('10', 'diamonds')
        self.card_kc = Card('K', 'clubs')
        self.card_qd = Card('Q','diamonds')
        self.card_jd = Card('J','diamonds')

    @parameterized.expand([
        (Card('2', 'spades'), 2),
        (Card('K', 'hearts'), 10),
        (Card('10', 'diamonds'), 10)
    ])
    def test_card_value_makes_sense(self, card, expected):
        self.assertEqual(card.points, expected)

    def test_can_sort_cards(self):
        cards = [self.card_10d, self.card_kh, self.card_2s]
        test_hand = sorted(cards)
        self.assertEqual(test_hand, [self.card_10d, self.card_kh, self.card_2s])

    def test_can_sort_same_value(self):
        cards = [self.card_kh, self.card_jd, self.card_10d, self.card_qd]
        test_hand = sorted(cards)
        self.assertEqual(test_hand, [self.card_10d, self.card_jd, self.card_qd, self.card_kh])

    def test_can_sort_suits(self):
        cards = [self.card_kh, self.card_kc]
        test_hand = sorted(cards)
        self.assertEqual(test_hand, [self.card_kc, self.card_kh])

if __name__ == '__main__':
    unittest.main()