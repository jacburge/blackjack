"""
This module contains various methods to handle currency.
"""

class NegativeValueError(Exception):
    """
    An exception type for when trying to add a negative, which is a no-no.
    """

class InsufficientFundsError(Exception):
    """
    The Wallet class manages money, and provides methods to add and remove money
    from the balance, as well as incorporating reasonable constraints on operations.
    """

class QuitCheatingError(Exception):
    """
    An exception to remind people that there are approved ways to modify the balance
    and stop cheating.
    """

class Wallet():
    """ See doc string above """
    accounts = {}

    def __init__(self, balance: float = 0):
        self._balance = balance

    def add_money(self, amount: float) -> float:
        """ Add the specified amount to our wallet. Returns the new balance. """
        if amount < 0:
            raise NegativeValueError('Amount must be positive')
        self._balance += amount
        return self._balance

    def remove_money(self, amount: float) -> float:
        """ Remove the specified amount from our wallet. Returns the new balance. """
        if amount < 0:
            raise NegativeValueError('Amount must be positive')
        if amount > self._balance:
            msg = f"If you remove that much you'll be bankrupt; balance: {self._balance}"
            raise InsufficientFundsError(msg)
        self._balance -= amount
        return self._balance

    @property
    def balance(self) -> float:
        """ Return the amount of money in the wallet."""
        return self._balance

    @balance.setter
    def balance(self, _: float) -> None:
        raise QuitCheatingError('Quit cheating! Use add_money() and '
                                'remove_money() to modify balance if'
                                'you must')