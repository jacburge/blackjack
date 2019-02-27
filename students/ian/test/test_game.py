import sys
sys.path.insert(0, '..')

import re
import unittest
from unittest.mock import MagicMock, Mock
from deck import Deck
from player import Player

import game
from card import Card

class TestGame(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player('Bob')

    def test_deal_cards(self):
        num_cards = 2
        game.deal_cards(self.deck, self.player, num_cards)
        self.assertEqual(num_cards, len(self.player.visible_cards))

    def test_basic_score_determination(self):
        self.player.add_card(Card('5', 'hearts'))
        self.player.add_card(Card('A', 'diamonds'))
        self.assertEqual(16, game.get_score(self.player))

    def test_blackjack_score_determination(self):
        self.player.add_card(Card('10', 'hearts'))
        self.player.add_card(Card('A', 'diamonds'))
        self.assertEqual(21, game.get_score(self.player))

    def test_harder_score_determination(self):
        self.player.add_card(Card('A', 'diamonds'))
        self.player.add_card(Card('A', 'clubs'))
        self.player.add_card(Card('10', 'hearts'))
        self.player.add_card(Card('7', 'diamonds'))
        self.assertEqual(19, game.get_score(self.player))

    def test_other_score_determination(self):
        self.player.add_card(Card('4', 'hearts'))
        self.player.add_card(Card('7', 'diamonds'))
        self.player.add_card(Card('A', 'clubs'))
        self.assertEqual(12, game.get_score(self.player))

    def test_ace_score_over_21(self):
        self.player.add_card(Card('10', 'hearts'))
        self.player.add_card(Card('10', 'diamonds'))
        self.player.add_card(Card('A', 'clubs'))
        self.player.add_card(Card('A', 'clubs'))
        self.assertEqual(22, game.get_score(self.player))

    def test_one_ace_11_and_one_1(self):
        self.player.add_card(Card('9', 'hearts'))
        self.player.add_card(Card('A', 'clubs'))
        self.player.add_card(Card('A', 'clubs'))
        self.assertEqual(21, game.get_score(self.player))

    def test_print_hand_prints_nicely(self):
        self.player.add_card(Card('9', 'hearts'))
        self.player.add_card(Card('4', 'diamonds'))
        expected = 'Your hand: 9 of Hearts, 4 of Diamonds'
        cardlist = game.get_cards(self.player)
        self.assertEqual(expected, cardlist)

    def test_get_bet_handles_happy_path(self):
        good_input = '12'
        game.say = MagicMock()
        game.get_input = MagicMock(return_value=good_input)
        amount = game.get_bet_amount(self.player)
        self.assertEqual(12.0, amount)

    def test_get_bet_handles_letter(self):
        good_input = '12'
        bad_input = 'twelve'
        game.say = MagicMock()
        game.get_input = MagicMock(side_effect=[bad_input, good_input])
        game.get_bet_amount(self.player)
        self.assertIn('twelve is not a number', str(game.say.mock_calls[-2]))


if __name__ == '__main__':
    unittest.main()
