"""
Test things around the mondey muduleself.
"""
import sys
sys.path.insert(0, '..')

import unittest
import money

class TestMoney(unittest.TestCase):
    def setUp(self):
        self.wallet = money.Wallet(100)

    def test_no_adding_negative_money(self):
        wallet =  money.Wallet(100)
        with self.assertRaises(money.NegativeValueError):
            wallet.add_money(-1)

    def test_remove_too_much_money(self):
        wallet = money.Wallet(100)
        with self.assertRaises(money.InsufficientFundsError):
            wallet.remove_money(101)

    def test_blanace_makes_sens(self):
        #self.wallet._balance = 1000000
        self.assertEqual(100,self.wallet.balance)

    def test_wallet_is_read_only(self):
        with self.assertRaises(money.QuiteCheatingError):
            self.wallet.balance = 1000000

if __name__ == '__main__':
    unittest.main()
