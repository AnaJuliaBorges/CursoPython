
class BankAccount:

    def __init__(self, number, holder, balance, limit):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def deposit(self, value):
        self.__balance += value

    def __limit_check(self, value):
        return value <= self.__balance + self.__limit

    def withdraw(self, value):
        if (self.__limit_check(value)):
            self.__balance -= value
        else:
            print(f"Não foi possível sacar o valor de R${value}")
            print(f"Valor disponível para saque: R${self.__balance + self.__limit}")

    def transfer(self, value, target):
        self.withdraw(value)
        target.deposit(value)

    def bank_statement(self):
        print(f"Titular: {self.__holder}, saldo: {self.__balance}")

    @property
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder

    @property
    def number(self):
        return self.__number

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_value):
        self.__limit = new_value

    @staticmethod
    def bank_code():
        return "007"

    @staticmethod
    def bank_code_list():
        return {'Agência': '001', 'Conta': '104', 'Bradesco': '237'}
