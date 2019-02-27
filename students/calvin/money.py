"""
This module dsecribes a Wallet class, which keeps track of money and allows debitsself. This assumes a single currency
"""

class NegativeValueError(Exception):
    """ an exception type for when trying to add a negative, which is a no-no """

class InsufficientFundsError(Exception):
    """ an exception to indicate the wallet doesn't have enought money to complete the requested transaction """

class QuiteCheatingError(Exception):
    """ dddd """

class Wallet():
    """ Wallet class """

    def __init__(self, balance: float = 0):
        self._balance: float = balance

    def add_money(self, amount: float) -> float:
        """ Add the specificed amount to our wallet. retrun the balance """
        if amount < 0:
            raise NegativeValueError('Amount must be positivie')
        self._balance += amount
        return self._balance

    def remove_money(self, amount: float) -> float:
        """ remove the specified amount. Return the new balance. """
        if amount < 0:
            raise NegativeValueError('Amount must be positivee')
        if amount > self._balance:
            msg = f'Insufficent funds in wallet; balance: {self._balance}'
            raise InsufficientFundsError(msg)
        self._balance -= amount
        return self._blance

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, amount: float) -> None:
        raise QuiteCheatingError('Quit cheating,'
                                ' please use the add_money() mehtod')
