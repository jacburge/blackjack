"""
This module describes a Wallet class, which keeps track of money and allows debits and credits.
"""

class NegativeValueError(Exception):
    """
    An exception type for when trying to add a negative, which is a no-no.
    """
class InsufficientFundsError(Exception):
    """
    An exception to indicate the wallet doesn't have enough money to complete the requested transaction
    """

class Wallet():
    """ Wallet class"""

    def __init__(self, balance: float = 0):
        self.balance: float = balance

    def add_money(self, amount: float) -> float:
        """ Add the specified amount to our wallet. Return the new balance."""
        if amount < 0:
            raise NegativeValueError('Amount must be positive')
        self.balance += amount
        return self.balance

    def remove_money(self, amount: float) -> float:
        """ Remove the specified amount. Return the new balance."""
        if amount < 0:
            raise NegativeValueError('Amount must be positive')
        if amount > self.balance:
            msg = f'Insufficient funds in wallet; balance:{self.balance}'
            raise InsufficientFundsError(msg)
        self.balance -= amount
        return self.balance
