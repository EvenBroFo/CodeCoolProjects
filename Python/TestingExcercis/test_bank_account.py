import pytest
from Bank_account import BankAccount


def test_initial_balance():
    account = BankAccount()
    assert account.get_balance() == 0


def test_deposit():
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100


def test_withdraw():
    account = BankAccount()
    account.deposit(100)
    account.withdraw(40)
    assert account.get_balance() == 60


def test_invalid_deposit():
    account = BankAccount()

    with pytest.raises(ValueError):
        account.deposit(-50)

    assert account.get_balance() == 0


def test_invalid_withdraw():
    account = BankAccount()
    account.deposit(100)

    with pytest.raises(ValueError):
        account.withdraw(150)

    assert account.get_balance() == 100

def test_zero_amounts():
    account = BankAccount()

    with pytest.raises(ValueError):
        account.deposit(0)

    with pytest.raises(ValueError):
        account.withdraw(0)

    assert account.get_balance() == 0