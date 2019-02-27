import sys
sys.path.insert(0, '..')

import unittest
import deck
import player
from card import Card

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.bob = player.Player('Bob')
        self.dealer = player.Player('Dealer', is_dealer=True)

    def test_add_cards_works(self):
        cards = [Card('K', 'hearts'), Card('2', 'diamonds')]
        for card in cards:
            self.bob.add_card(card)
        self.assertEqual(cards, self.bob.visible_cards)

    def test_player_points_are_good(self):
        self.bob.add_card(Card('K', 'hearts'))
        self.bob.add_card(Card('2', 'hearts'))
        self.assertEqual(12, self.bob.get_points())

    def test_dealer_points_are_good(self):
        self.dealer.add_card(Card('K', 'hearts'))
        self.dealer.add_card(Card('2', 'hearts'))
        # first card is hidden from view for dealers
        self.assertEqual(2, self.dealer.get_points())
        self.assertEqual(12, self.dealer.get_points(include_facedown=True))

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

    def test_dealer_point_total_is_sensible(self):
        self.dealer.add_card(Card('4', 'hearts'))
        self.dealer.add_card(Card('A', 'diamonds'))
        expected_points = 15
        self.assertEqual(expected_points,
                         self.dealer.get_points(include_facedown=True))

if __name__ == '__main__':
    unittest.main()
