# -- Decorators

class SuperAccount():
    __balance: float = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Amount can't be negative!")

        self.__balance = amount
        return self.__balance

    @property
    def balance_formatted(self):
        return f"{self.__balance} €"


paul_account = SuperAccount()

paul_account.balance = 10
print(paul_account.balance)
print(paul_account.balance_formatted)

exit()
# ----


class Account():

    __balance: float

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount < 0:
            raise ValueError("Amount can't be negative!")

        self.__balance = amount
        return self.__balance


marie_account = Account()
marie_account.set_balance(1000)

marie_account.balance = 10
print(marie_account.balance)


# marie_account.__balance = 100
# print(marie_account.get_balance())

# print(marie_account.get_balance())
# print(marie_account.__balance)
