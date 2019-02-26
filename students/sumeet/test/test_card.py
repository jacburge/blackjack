""" run tests on Card functionality """

import unittest
import sys
sys.path.insert(0, '..')

from card import Card # pylint: disable=wrong-import-position

class TestCard(unittest.TestCase):

    def test_card_value_makes_sense(self):
        card_2 = Card('2', 'spades')
        card_k = Card('K', 'hearts')
        card_10 = Card('10', 'diamonds')
        self.assertEqual(2, card_2.value())
        self.assertEqual(10, card_10.value())
        self.assertEqual(10, card_k.value())


if __name__ == '__main__':
    unittest.main()
