# exercises/bank_account.py

class BankAccount:
    """
    A basic bank account that can handle deposits and withdrawals.

    This class should:
    - Maintain an accurate balance
    - Prevent overdrafts (negative balances)
    - Handle deposits and withdrawals safely

    Think about: How do you validate input amounts? What should happen with invalid amounts?
    How do you ensure the balance never goes negative?
    """

    def __init__(self, owner: str, opening_balance: float) -> None:
        """
        Create a new bank account.

        :param owner: the account holder's name
        :param opening_balance: the initial deposit amount

        TODO: Initialize the bank account
        """
        raise NotImplementedError()

    def deposit(self, amount: float) -> bool:
        """
        Add money to the account.

        :param amount: the amount to deposit
        :return: True if deposit was successful, False otherwise

        TODO: Implement deposit functionality
        """
        raise NotImplementedError()

    def withdraw(self, amount: float) -> bool:
        """
        Remove money from the account.

        :param amount: the amount to withdraw
        :return: True if withdrawal was successful, False if it would cause overdraft

        TODO: Implement withdrawal with overdraft protection
        """
        # prevent overdraft
        raise NotImplementedError()

    def get_balance(self) -> float:
        return self.balance
