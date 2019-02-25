import sys
sys.path.insert(0, '..')

import unittest
from deck import Deck
from player import Player
import game
from card import Card

class TestGame(unittest.TestCase):

    def test_deal_cards(self):
        test_deck = Deck()
        test_deck.shuffle()
        test_player = Player('Bob')
        num_cards = 2
        game.deal_cards(test_deck, test_player, num_cards)
        self.assertEqual(num_cards, len(test_player.visible_cards()))

    def test_basic_score_determination(self):
        test_deck = Deck()
        test_deck.shuffle()
        test_player = Player('Bob')
        test_player.add_card(Card('5', 'hearts'))
        test_player.add_card(Card('A', 'diamonds'))
        self.assertEqual(16, game.get_score(test_player))

    def test_blackjack_score_determination(self):
        test_deck = Deck()
        test_deck.shuffle()
        test_player = Player('Bob')
        test_player.add_card(Card('10', 'hearts'))
        test_player.add_card(Card('A', 'diamonds'))
        self.assertEqual(21, game.get_score(test_player))

    def test_harder_score_determination(self):
        test_deck = Deck()
        test_deck.shuffle()
        test_player = Player('Bob')
        test_player.add_card(Card('A', 'diamonds'))
        test_player.add_card(Card('A', 'clubs'))
        test_player.add_card(Card('10', 'hearts'))
        test_player.add_card(Card('7', 'diamonds'))
        self.assertEqual(19, game.get_score(test_player))

    def test_other_score_determination(self):
        test_deck = Deck()
        test_deck.shuffle()
        test_player = Player('Bob')
        test_player.add_card(Card('4', 'hearts'))
        test_player.add_card(Card('7', 'diamonds'))
        test_player.add_card(Card('A', 'clubs'))
        self.assertEqual(12, game.get_score(test_player))

    def test_ace_score_over_21(self):
        test_deck = Deck()
        test_deck.shuffle()
        test_player = Player('Bob')
        test_player.add_card(Card('10', 'hearts'))
        test_player.add_card(Card('10', 'diamonds'))
        test_player.add_card(Card('A', 'clubs'))
        test_player.add_card(Card('A', 'clubs'))
        self.assertEqual(22, game.get_score(test_player))

    def test_one_ace_11_and_one_1(self):
        test_deck = Deck()
        test_deck.shuffle()
        test_player = Player('Bob')
        test_player.add_card(Card('9', 'hearts'))
        test_player.add_card(Card('A', 'clubs'))
        test_player.add_card(Card('A', 'clubs'))
        self.assertEqual(21, game.get_score(test_player))


if __name__ == '__main__':
    unittest.main()
