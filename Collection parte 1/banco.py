from abc import ABCMeta, abstractmethod
from functools import total_ordering

@total_ordering
class Account(metaclass=ABCMeta):
    def __init__(self, code):
       self.code = code
       self.balance = 0

    def deposit(self, value):
        self.balance += value

    def __str__(self):
        return f"Conta de número {self.code}, saldo: R${self.balance}"

    @abstractmethod
    def next_month(self):
        pass

    def __eq__(self, other):
        if (type(other) != Account):
            return False

        return self.code == other.code and self.balance == other.balance

    def __lt__(self, other):
        if self.balance != other.balance:
            return self.balance < other.balance

        return self.code < other.code


class CheckingAccount(Account):

    def next_month(self):
        self.balance -= 2


class SavingAccount(Account):

    def next_month(self):
        self.balance *= 1.01
        self.balance -= 3


class InvestimentAccount(Account):
    pass


