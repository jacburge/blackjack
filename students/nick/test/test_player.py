import sys
sys.path.insert(0, '..')

import unittest
import player
from card import Card

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.p1 = player.Player('Bob')
        self.dealer = player.Player('Dallas', is_dealer=True)

    def test_add_cards_works(self):
        cards = [Card('K', 'hearts'), Card('2', 'diamonds')]
        for card in cards:
            self.p1.add_card(card)
        self.assertEqual(cards, self.p1.visible_cards)

    def test_dealer_card_is_hidden(self):
        visible_card = Card('2', 'hearts')
        self.dealer.add_card(Card('K', 'hearts'))
        self.dealer.add_card(visible_card)
        self.assertEqual([visible_card], self.dealer.visible_cards)

    def test_all_cards_works_for_dealer(self):
        hidden_card = Card('K', 'hearts')
        visible_card = Card('2', 'hearts')
        self.dealer.add_card(hidden_card)
        self.dealer.add_card(visible_card)
        self.assertIn(hidden_card, self.dealer.all_cards)
        self.assertEqual(2, len(self.dealer.all_cards))

    def test_all_cards_pretty_print(self):
        hidden_card = Card('K', 'hearts')
        visible_card = Card('2', 'hearts')
        self.dealer.add_card(hidden_card)
        self.dealer.add_card(visible_card)

        # the hidden card gets printed last, by design
        expected = '2 of Hearts, K of Hearts'
        self.assertEqual(expected, self.dealer.all_cards_printable)

if __name__ == '__main__':
    unittest.main()
