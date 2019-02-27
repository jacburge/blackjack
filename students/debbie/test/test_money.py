"""
Test things around the money module.
"""

import unittest
import money

class TestMoney(unittest.TestCase):
    def setUp(self):
        self.wallet = money.Wallet(100)

    def test_no_adding_negative_moneys(self):
        with self.assertRaises(money.NegativeValueError):
            self.wallet.add_money(-1)

    def test_remove_too_much_money(self):
        wallet = money.Wallet(100)
        with self.assertRaises(money.InsufficientFundsError):
            self.wallet.remove_money(101)

    def test_balance_makes_sense(self):
        self.assertEqual(100, self.wallet.balance)

    def test_wallet_balance_is_read_only(self):
        with self.assertRaises(money.QuitCheatingError):
            self.wallet.balance = 1000000

