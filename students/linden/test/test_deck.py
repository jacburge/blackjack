import deck
""" run tests on Deck functionality """

import unittest
import sys
sys.path.insert(0, '..')


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

    def test_dealt_cards_are_different(self):
        ''' Only supports single deck testing of the deal function. '''
        test_deck = deck.Deck()

        dealt_cards = [test_deck.deal() for _ in range(10)]
        # dealt_cards=[]  # done is list comprehension above
        # for _ in range(10):
        #     dealt_cards.append(test_deck.deal())
        set_cards = set(dealt_cards)  # remove duplicate entries
        # if we have a list of identical cards, the length of the set would be 1
        self.assertEqual(len(dealt_cards), len(set_cards),"Returns duplicates and shouldn't")


if __name__ == '__main__':
    unittest.main()
