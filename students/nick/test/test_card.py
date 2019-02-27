""" run tests on Card functionality """

import unittest
import sys
sys.path.insert(0, '..')

from card import Card # pylint: disable=wrong-import-position

class TestCard(unittest.TestCase):

    def setUp(self) -> None:
        self.cards = [Card('2', 'spades'), Card('K', 'hearts'), Card('10', 'diamonds')]

    def test_card_points_make_sense(self):
        self.assertEqual(2, self.cards[0].points)
        self.assertEqual(10, self.cards[1].points)
        self.assertEqual(10, self.cards[2].points)
    
    def test_cards_can_be_sorted_by_suit(self):
        expected = '10 of Diamonds, K of Hearts, 2 of Spades'
        self.assertEqual(expected, ', '.join(str(card) for card in sorted(self.cards)))
    
    def test_cards_can_be_sorted_within_rank(self):
        for card in self.cards:
            card.suit = 'diamonds'

        expected = '2 of Diamonds, 10 of Diamonds, K of Diamonds'
        self.assertEqual(expected, ', '.join(str(card) for card in sorted(self.cards)))


if __name__ == '__main__':
    unittest.main()
