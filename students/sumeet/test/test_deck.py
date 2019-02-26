""" run tests on Deck functionality """

import unittest
import sys
sys.path.insert(0, '..')

import deck # pylint: disable=wrong-import-position

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = deck.Deck()

    def test_number_of_cards_in_init(self):
        """ test that the number of cards in a single-deck init is
        sensible """
        self.assertEqual(52, len(self.deck))

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
        first_ten = self.deck[:10]
        self.deck.shuffle()
        shuffled_ten = self.deck[:10]
        self.assertNotEqual(first_ten, shuffled_ten)

    def test_dealt_cards_are_different(self):
        self.deck.shuffle()
        card1 = self.deck.deal()
        card2 = self.deck.deal()
        self.assertNotEqual((card1.rank, card1.suit),
                            (card2.rank, card2.suit))


if __name__ == '__main__':
    unittest.main()
