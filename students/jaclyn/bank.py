"""
This module describes a Bank class, which keeps track of money
and allows debits and credits. Assuming a single currency.
"""

class NegativeValueError(Exception):
    """
    An exception type for when trying to add a negative, which is a no-no.
    """

class InsufficientFundsError(Exception):
    """
    An exception to indicate the wallet doesn't have enough money to complete
    the requested transaction.
    """

class Wallet():
    """ See doc string above """
    accounts = {}

    def __init__(self, balance: float = 0):
        self.balance = balance

    def add_money(self, amount: float) -> float:
        """ Add the specified amount to our wallet. Returns the new balance. """
        if amount < 0:
            raise NegativeValueError('Amount must be positive')
        self.balance += amount
        return self.balance

    def remove_money(self, amount: float) -> float:
        """ Remove the specified amount from our wallet. Returns the new balance. """
        if amount < 0:
            raise NegativeValueError('Amount must be positive')
        if amount > self.balance:
            msg = f"If you remove that much you'll be bankrupt; balance: {self.balance}"
            raise InsufficientFundsError(msg)
        self.balance -= amount
        return self.balance
