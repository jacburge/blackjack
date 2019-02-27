"""
This Wallet class manages money and provides methods to add and remove money from the balance,
as well as incorporating reasonable constraints on operations.
"""

class NegativeValueError(Exception):
    """ An exception type for when trying to add a negative, which is a no-no"""

class InsufficientFundsError(Exception):
    """
    An exception to indicate the wallet doesn't have enough money to complete the requested transaction.
    """

class QuitCheatingError(Exception):
    """
    An exception to remind people that there are approved ways to modify the balance.
    """


class Wallet():
    """ Wallet class """

    def __init__(self, balance: float = 0):
        self._balance: float = balance

    def add_money(selfself, amount: float) -> float:
        """ Add the specified amount to our wallet. Return the new balance. """
        if amount < 0:
            raise NegativeValueError('Amount must be positive')
        self._balance += amount
        return self._balance

    def remove_money(self, amount: float) -> float:
        """ Remove the specified amount from our wallet. Return the new balance. """
        if amount < 0:
            raise NegativeValueError('Amount must be positive')
        if amount > self._balance:
            msg = f'Insufficient funds in wallet; balance: {self._balance}'
            raise InsufficientFundsError(msg)
        self._balance -= amount
        return self._balance

    @property
    def balance(self) -> float:
        """ Return the amount of money in the wallet."""
        return self._balance

    @balance.setter
    def balance(self, _: float) -> None:
        raise QuitCheatingError('Please use the add_money() and '
                                'remove_money() methods to modify the balance')