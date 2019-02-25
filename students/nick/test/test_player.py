import sys
sys.path.insert(0, '..')

import unittest
import deck
import player
from card import Card

class TestPlayer(unittest.TestCase):

    def test_add_cards_works(self):
        test_player = player.Player('Bob')
        cards = [Card('K', 'hearts'), Card('2', 'diamonds')]
        for card in cards:
            test_player.add_card(card)
        self.assertEqual(cards, test_player.visible_cards())

    def test_player_points_are_good(self):
        test_player = player.Player('Bob')
        test_player.add_card(Card('K', 'hearts'))
        test_player.add_card(Card('2', 'hearts'))
        self.assertEqual(12, test_player.points())

    def test_dealer_points_are_good(self):
        test_player = player.Player('Bob', True)
        test_player.add_card(Card('K', 'hearts'))
        test_player.add_card(Card('2', 'hearts'))
        # first card is hidden from view for dealers
        self.assertEqual(2, test_player.points())
        self.assertEqual(12, test_player.points(include_facedown=True))

    def test_dealer_card_is_hidden(self):
        test_player = player.Player('Bob', is_dealer=True)
        visible_card = Card('2', 'hearts')
        test_player.add_card(Card('K', 'hearts'))
        test_player.add_card(visible_card)
        self.assertEqual([visible_card], test_player.visible_cards())

    def test_all_cards_works_for_dealer(self):
        test_player = player.Player('Bob', is_dealer=True)
        hidden_card = Card('K', 'hearts')
        visible_card = Card('2', 'hearts')
        test_player.add_card(hidden_card)
        test_player.add_card(visible_card)
        self.assertIn(hidden_card, test_player.all_cards())
        self.assertEqual(2, len(test_player.all_cards()))

if __name__ == '__main__':
    unittest.main()
