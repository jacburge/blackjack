"""
Test functionality of the money module
"""

import sys
sys.path.insert(0, '..')

import unittest
import money

class TestMoney(unittest.TestCase):

    def setUp(self):
        self.wallet = money.Wallet(100)

    def test_no_addding_negative_value(self):
        with self.assertRaises(money.NegativeValueError):
            self.wallet.add_credit(-1)

    def test_no_removing_insufficient_funds(self):
        with self.assertRaises(money.NSFError):
            self.wallet.pay_debt(101)
    
    def test_addint_makes_sense(self):
        self.wallet.add_credit(50)
        self.assertEqual(150, self.wallet.balance)
    
    def test_balance_is_read_only(self):
        with self.assertRaises(AttributeError):
            self.wallet.balance = 1000000
    
    def test_transfer_to_makes_sense(self):
        o_wallet = money.Wallet(25)
        self.wallet.transfer_to(o_wallet, 25)
        self.assertEqual(75, self.wallet.balance)
        self.assertEqual(50, o_wallet.balance)

if __name__ == '__main__':
    unittest.main()
