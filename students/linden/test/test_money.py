""" run tests on Wallet functionality """

import sys
import unittest

from money import (InsufficientFundsError, NegativeValueError,
                   QuitCheatingError, Wallet)

sys.path.insert(0, '..')  # Tells Python where to find the money module


class TestMoney(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet(100)

    def test_add_negative_money(self):
        with self.assertRaises(NegativeValueError):
            self.wallet.add_money(-1)

    def test_remove_more_money_than_balance(self):
        with self.assertRaises(InsufficientFundsError):
            self.wallet.remove_money(101)

    def test_balance_in_equals_balance(self):
        self.assertEqual(100, self.wallet.balance)

    def test_wallet_is_read_only(self):
        with self.assertRaises(QuitCheatingError):
            self.wallet.balance = 1000000
