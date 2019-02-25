import sys
sys.path.insert(0, '..')

import unittest
from deck import Deck
from player import Player
import game
from card import Card

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.player = Player('Bob')
        self.deck.shuffle()

    def test_deal_cards(self):
        #self.deck = Deck()
        #self.deck.shuffle()
        #self.player = Player('Bob')
        num_cards = 2
        game.deal_cards(self.deck, self.player, num_cards)
        self.assertEqual(num_cards, len(self.player.visible_cards()))

    def test_basic_score_determination(self):
        #self.deck = Deck()
        #self.deck.shuffle()
        #self.player = Player('Bob')
        self.player.add_card(Card('5', 'hearts'))
        self.player.add_card(Card('A', 'diamonds'))
        self.assertEqual(16, game.get_score(self.player))

    def test_blackjack_score_determination(self):
        #self.deck = Deck()
        #self.deck.shuffle()
        #self.player = Player('Bob')
        #self.player.add_card(Card('10', 'hearts'))
        self.player.add_card(Card('10', 'hearts'))
        #self.player.add_card(Card('A', 'diamonds'))
        self.player.add_card(Card('A', 'diamonds'))
        self.assertEqual(21, game.get_score(self.player))

    def test_harder_score_determination(self):
        #self.deck = Deck()
        #self.deck.shuffle()
        #self.player = Player('Bob')
        self.player.add_card(Card('A', 'diamonds'))
        self.player.add_card(Card('A', 'clubs'))
        self.player.add_card(Card('10', 'hearts'))
        self.player.add_card(Card('7', 'diamonds'))
        self.assertEqual(19, game.get_score(self.player))

    def test_other_score_determination(self):
        #self.deck = Deck()
        #self.deck.shuffle()
        #self.player = Player('Bob')
        self.player.add_card(Card('4', 'hearts'))
        self.player.add_card(Card('7', 'diamonds'))
        self.player.add_card(Card('A', 'clubs'))
        self.assertEqual(12, game.get_score(self.player))

    def test_ace_score_over_21(self):
        #self.deck = Deck()
        #self.deck.shuffle()
        #self.player = Player('Bob')
        self.player.add_card(Card('10', 'hearts'))
        self.player.add_card(Card('10', 'diamonds'))
        self.player.add_card(Card('A', 'clubs'))
        self.player.add_card(Card('A', 'clubs'))
        self.assertEqual(22, game.get_score(self.player))

    def test_one_ace_11_and_one_1(self):
        #self.deck = Deck()
        #self.deck.shuffle()
        #self.player = Player('Bob')
        self.player.add_card(Card('9', 'hearts'))
        self.player.add_card(Card('A', 'clubs'))
        self.player.add_card(Card('A', 'clubs'))
        self.assertEqual(21, game.get_score(self.player))


if __name__ == '__main__':
    unittest.main()
