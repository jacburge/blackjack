""" run tests on Deck functionality """

import unittest
import sys
sys.path.insert(0, '..')

import deck # pylint: disable=wrong-import-position

class TestDeck(unittest.TestCase):

    def test_number_of_cards_in_init(self):
        """ test that the number of cards in a single-deck init is
        sensible """
        test_deck = deck.Deck()
        self.assertEqual(52, len(test_deck))

    def test_multiple_decks(self):
        """ test that the number of cards in a multiple-deck init is
        sensible """
        num_decks = 3
        test_deck = deck.Deck(num_decks)
        self.assertEqual(52 * num_decks, len(test_deck))

    def test_card_order_changes_on_shuffle(self):
        """ note: there is a vanishingly small chance this test will
        fail even with perfectly valid code, if somehow the shuffle()
        function returns the list in the same order.  run the test again
        if this test fails once."""
        test_deck = deck.Deck()
        first_ten = test_deck[:10]
        test_deck.shuffle()
        shuffled_ten = test_deck[:10]
        self.assertNotEqual(first_ten, shuffled_ten)


if __name__ == '__main__':
    unittest.main()
