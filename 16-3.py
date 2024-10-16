# BankAccount class with encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute for account number
        self.__balance = balance  # Private attribute for balance

    # Public method to display account information
    def get_account_info(self):
    # TODO: Print the account number
        return self.__account_number
    # Getter for balance
    def get_balance(self):
        # TODO: Return the balance (private attribute)
        return self.__balance

    # Method to deposit money, with validation
    def deposit(self, amount):
        # TODO: If amount is positive, add it to the balance and print a success message
        if amount > 0:
            self.__balance += amount
        # TODO: Otherwise, print an error message saying deposit amount must be positive
        else:
            print(f"ERROR: value must be positive")
        return self.__balance

    # Method to withdraw money, with validation
    def withdraw(self, amount):
        # TODO: If amount is positive and does not exceed the balance, subtract it from the balance
        if 0 < amount < self.__balance:
            self.__balance = self.__balance - amount
        # TODO: Otherwise, print an error message saying withdrawal is invalid
        else:
            print(f"ERROR: withdrawal is invalid")
        return self.__balance


# SavingsAccount subclass
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    # Overriding withdraw method to prevent balance from going below zero
    def withdraw(self, amount):
        # TODO: Check if the amount does not exceed the balance before calling the super class's withdraw method
        if amount < self.__balance:
            super().withdraw(amount)



        # TODO: If insufficient funds, print an error message
        pass

    # Method to apply interest
    def apply_interest(self):
        # TODO: Calculate interest based on the balance and interest rate
        # TODO: Add the interest to the balance using the deposit method
        pass


# CheckingAccount subclass
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, withdrawal_fee):
        super().__init__(account_number, balance)
        self.withdrawal_fee = withdrawal_fee

    # Overriding withdraw method to deduct a fee on every withdrawal
    def withdraw(self, amount):
        # TODO: Calculate the total amount including the withdrawal fee
        # TODO: If sufficient funds, subtract the total amount from the balance by calling the super class's withdraw method
        # TODO: Print a message indicating that the withdrawal fee has been applied
        pass


# Test the classes
savings = SavingsAccount("123456", 1000, 0.05)
checking = CheckingAccount("789012", 500, 2)

# Display account info and perform transactions
# savings.get_account_info()
# savings.deposit(200)
# savings.withdraw(150)
# savings.apply_interest()

# checking.get_account_info()
# checking.deposit(300)
# checking.withdraw(50)
# checking.withdraw(800)  # Invalid withdrawal, insufficient funds
