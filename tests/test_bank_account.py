# tests/test_bank_account.py

from exercises.bank_account import BankAccount


def test_deposit_withdraw_flow():
    acc = BankAccount("Rens", 100)
    assert acc.deposit(50) is True
    assert acc.withdraw(200) is False
    assert acc.withdraw(120) is True
    assert acc.get_balance() == 30
