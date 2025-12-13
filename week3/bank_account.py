class BankAcount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successfully")
        else:
            print("Amount must be positive")

    def with_draw(self, amount):
        if amount >= self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdraw successfully")

    def get_balance(self):
        return self.__balance


def main():
    account = BankAcount()
    account.with_draw(amount=100)
    print("Current Balance", account.get_balance())
    account.deposit(-100)

    account.deposit(amount=500)
    print("Current Balance", account.get_balance())
    account.with_draw(200)
    print("Current Balance", account.get_balance())


if __name__ == "__main__":
    main()
