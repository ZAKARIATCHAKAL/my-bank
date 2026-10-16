from client import Client, client_deposit, transfer_client
from project import superficial_design, intermediate_design_client, workers_design

def test_deposit():

    client = Client(
        "Zakaria Tchakal",
        "2005/09/13",
        "12345678901234567890",
        "+213 555 555 555",
        1000,
        "123456",
        0
    )

    client.deposit(500)

    assert client.balance == 1500


def test_withdraw():

    client = Client(
        "Zakaria Tchakal",
        "2005/09/13",
        "12345678901234567890",
        "+213 555 555 555",
        1000,
        "123456",
        0
    )

    client.withdraw(300)

    assert client.balance == 700


def test_borrowing():

    client = Client(
        "Zakaria Tchakal",
        "2005/09/13",
        "12345678901234567890",
        "+213 555 555 555",
        1000,
        "123456",
        200
    )

    client.borrowing(500)

    assert client.debts == 700


def test_client_deposit(monkeypatch):

    client = Client(
        "Zakaria Tchakal",
        "2005/09/13",
        "12345678901234567890",
        "+213 555 555 555",
        1000,
        "123456",
        0
    )

    ls = [client]

    monkeypatch.setattr(
        "builtins.input",
        lambda x: "123456"
    )

    client_deposit(
        ls,
        "Zakaria Tchakal",
        "12345678901234567890",
        500
    )

    assert client.balance == 1500


def test_transfer_client(monkeypatch):

    client_1 = Client(
        "Zakaria Sender",
        "2005/09/13",
        "11111111111111111111",
        "+213 555 555 555",
        1000,
        "123456",
        0
    )

    client_2 = Client(
        "Zakaria Receiver",
        "2005/09/13",
        "22222222222222222222",
        "+213 555 555 555",
        200,
        "654321",
        0
    )

    ls = [client_1, client_2]

    monkeypatch.setattr(
        "builtins.input",
        lambda x: "123456"
    )

    transfer_client(
        ls,
        "Zakaria Sender",
        "11111111111111111111",
        "Zakaria Receiver",
        "22222222222222222222",
        300
    )

    assert client_1.balance == 700
    assert client_2.balance == 500


def test_superficial_design_valid_first_try(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "Customer Use")
    assert superficial_design() == "Customer Use"


def test_superficial_design_invalid_then_valid(monkeypatch):

    inputs = iter(["Invalid Option", "Employee Use"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert superficial_design() == "Employee Use"




def test_intermediate_design_client_valid(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "Withdraw money")
    assert intermediate_design_client() == "Withdraw money"


def test_intermediate_design_client_retry(monkeypatch):

    inputs = iter(["1", "Deposit money"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert intermediate_design_client() == "Deposit money"


def test_workers_design_valid(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "Accounting Department")
    assert workers_design() == "Accounting Department"


def test_workers_design_retry(monkeypatch):

    inputs = iter(["Wrong Choice", "New Worker"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert workers_design() == "New Worker"
