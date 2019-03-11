import sys
sys.path.insert(0, '..')

import unittest
from unittest.mock import MagicMock, Mock
from deck import Deck
import player
import game
from card import Card

class TestGame(unittest.TestCase):

    def setUp(self):
        self.bob = player.Player('Bob')
        self.dealer = player.Player('Dealer', is_dealer=True)
        self.deck = Deck()
        self.deck.shuffle()

    def test_deal_cards(self):
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

    def test_clean_print_cards(self):
        self.bob.add_card(Card('9', 'hearts'))
        expected = '{}: {}'.format(self.bob.name, "Your hand: ['9 of Hearts']")
        reality = game.print_cards(self.bob)
        self.assertEqual(expected,reality)

    def test_get_bet_handles_proper_input(self):
        good_input = '12'
        game.say = MagicMock()
        game.get_input = MagicMock(return_value = good_input)
        amount = game.get_bet_amount(self.bob)
        self.assertEqual(12.0, amount)

    def test_get_bet_handles_hoomans(self):
        good_input = '12'
        bad_input = 'twelve'
        game.say = MagicMock()
        game.get_input = Mock(side_effect = [bad_input, good_input])
        game.get_bet_amount(self.bob)
        # import pdb; pdb.set_trace()
        self.assertIn(f'{bad_input} is not a number, try again', str(game.say.mock_calls[-1]))

if __name__ == '__main__':
    unittest.main()
