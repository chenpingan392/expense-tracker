from app.models import Transaction


def test_create_transaction():
    transaction = Transaction(
        "支出",
        25,
        "餐饮",
        "午餐"
    )

    assert transaction.transaction_type == "支出"
    assert transaction.amount == 25
    assert transaction.category == "餐饮"
    assert transaction.note == "午餐"


def test_transaction_to_dict():
    transaction = Transaction(
        "支出",
        25,
        "餐饮",
        "午餐"
    )

    data = transaction.to_dict()

    assert data == {
        "transaction_type": "支出",
        "amount": 25,
        "category": "餐饮",
        "note": "午餐"
    }


def test_transaction_from_dict():
    data = {
        "transaction_type": "收入",
        "amount": 3000,
        "category": "工资",
        "note": "七月工资"
    }

    transaction = Transaction.from_dict(data)

    assert transaction.transaction_type == "收入"
    assert transaction.amount == 3000
    assert transaction.category == "工资"
    assert transaction.note == "七月工资"