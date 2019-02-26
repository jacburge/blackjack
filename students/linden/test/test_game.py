import sys
import unittest

import game
from card import Card
from deck import Deck
from player import Player

sys.path.insert(0, '..')


class TestGame(unittest.TestCase):

    def setUp(self):
        self.bob = Player('Bob')
        self.dealer = Player('Dealer', is_dealer=True)
        self.test_deck = Deck()
        self.test_deck.shuffle()

    def test_format_cards(self):
        #10-diamonds 10, J-diamonds 10
        self.bob.add_card(Card('10', 'diamonds'))
        self.bob.add_card(Card('J', 'diamonds'))
        self.assertEqual("10-diamonds 10, J-diamonds 10", game.format_cards(self.bob))

    def test_deal_cards(self):
        num_cards = 2
        game.deal_cards(self.test_deck, self.bob, num_cards)
        self.assertEqual(num_cards, len(self.bob.visible_cards()))

    def test_basic_score_determination(self):
        self.bob.add_card(Card('5', 'hearts'))
        self.bob.add_card(Card('A', 'diamonds'))
        self.assertEqual(16, game.get_score(self.bob))

    def test_blackjack_score_determination(self):
        self.bob.add_card(Card('10', 'hearts'))
        self.bob.add_card(Card('A', 'diamonds'))
        self.assertEqual(21, game.get_score(self.bob))

    def test_harder_score_determination(self):
        self.bob.add_card(Card('A', 'diamonds'))
        self.bob.add_card(Card('A', 'clubs'))
        self.bob.add_card(Card('10', 'hearts'))
        self.bob.add_card(Card('7', 'diamonds'))
        self.assertEqual(19, game.get_score(self.bob))

    def test_other_score_determination(self):
        self.bob.add_card(Card('4', 'hearts'))
        self.bob.add_card(Card('7', 'diamonds'))
        self.bob.add_card(Card('A', 'clubs'))
        self.assertEqual(12, game.get_score(self.bob))

    def test_ace_score_over_21(self):
        self.bob.add_card(Card('10', 'hearts'))
        self.bob.add_card(Card('10', 'diamonds'))
        self.bob.add_card(Card('A', 'clubs'))
        self.bob.add_card(Card('A', 'clubs'))
        self.assertEqual(22, game.get_score(self.bob))

    def test_one_ace_11_and_one_1(self):
        self.bob.add_card(Card('9', 'hearts'))
        self.bob.add_card(Card('A', 'clubs'))
        self.bob.add_card(Card('A', 'clubs'))
        self.assertEqual(21, game.get_score(self.bob))


if __name__ == '__main__':
    unittest.main()
