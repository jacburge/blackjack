'''
This module describes a Bank Class that tracks money and allows debits and credits.
This assumes a single currency.
'''


class NegativeValueError(Exception):
    """ Exception type for when trying to add a negative, which is a no-no. """


class InsufficientFundsError(Exception):
    """ Exception type for when trying to remove more money than you have. """


class QuitCheatingError(Exception):
    """ Exception type for when trying to directly access balance instead of
        using add_money or remove_money. 
    """


class Wallet():
    ''' Bank Class '''

    def __init__(self, balance: float = 0):
        self._balance = balance

    def add_money(self, amount: float) -> float:
        ''' Add the specified amount to the wallet. Return new balance. '''
        # TODO  add txns in log and check for negative, etc.
        if amount < 0:
            raise NegativeValueError('Amount must be positive.')

        self._balance += amount
        return self._balance

    def remove_money(self, amount: float) -> float:
        ''' Subtract the amount from the balance and return new balance.None
        Throws exception.'''
        # TODO  add txns in log and check for negative, etc.
        if amount < 0:
            raise NegativeValueError('Amount must be positive.')
        if amount > self._balance:
            msg = f'Insufficient funds in wallet. Balance: {self._balance}'
            raise InsufficientFundsError(msg)
        self._balance -= amount
        return self._balance

    @property
    def balance(self) -> float:
            ''' Return the amount of money in the waller. '''
            return self._balance

    @balance.setter
    def balance(self, amount: float) -> None:
        raise QuitCheatingError('Use the add_money() method instead.')
