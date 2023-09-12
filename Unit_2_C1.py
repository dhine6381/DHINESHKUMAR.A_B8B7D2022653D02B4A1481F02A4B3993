class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance:.2f}")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance:.2f}")


# Test the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    my_account = BankAccount("123456789", "Dhineshkumar A ", 1000.0)

    # Display initial balance
    my_account.display_balance()

    # Deposit some money
    my_account.deposit(500.0)

    # Withdraw some money
    my_account.withdraw(200.0)

    # Try to withdraw more money than the balance
    my_account.withdraw(1500.0)

    # Display the final balance
    my_account.display_balance()
