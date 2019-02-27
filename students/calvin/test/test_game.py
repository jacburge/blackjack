import sys
sys.path.insert(0, '..')

import unittest
from unittest.mock import MagicMock, Mock
from deck import Deck
from player import Player
import game
from card import Card

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.bob = Player('Bob')

    def test_deal_cards(self):
        #test_deck = Deck()
        #test_deck.shuffle()
        #test_player = Player('Bob')
        num_cards = 2
        game.deal_cards(self.deck, self.bob, num_cards)
        self.assertEqual(num_cards, len(self.bob.visible_cards))

    def test_basic_score_determination(self):
        self.bob.add_card(Card('5', 'hearts'))
        self.bob.add_card(Card('A', 'diamonds'))
        self.assertEqual(16, game.get_score(self.bob))

    def test_blackjack_score_determination(self):
        self.bob.add_card(Card('10', 'hearts'))
        self.bob.add_card(Card('A', 'diamonds'))
        self.assertEqual(21, game.get_score(self.bob))

    def test_harder_score_determination(self):
        self.bob = Player('Bob')
        self.bob.add_card(Card('A', 'diamonds'))
        self.bob.add_card(Card('A', 'clubs'))
        self.bob.add_card(Card('10', 'hearts'))
        self.bob.add_card(Card('7', 'diamonds'))
        self.assertEqual(19, game.get_score(self.bob))

    def test_other_score_determination(self):
        self.bob = Player('Bob')
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

    def test_get_bet_handles_letter(self):
        good_input = '12'
        bad_input = 'twelve'
        game.say = MagicMock()
        game.get_input = MagicMock(side_effect=[bad_input, good_input])
        game.get_bet_amount(self.bob)
        self.assertIn('twelve is not a number', str(game.say.mock_calls[-2]))

if __name__ == '__main__':
    unittest.main()
