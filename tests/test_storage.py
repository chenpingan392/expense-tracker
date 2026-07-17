from pathlib import Path

from app.models import Transaction
from app.storage import load_transactions, save_transactions


def test_save_and_load_transactions(tmp_path: Path):
    file_path = tmp_path / "transactions.json"

    original_transactions = [
        Transaction("支出", 25, "餐饮", "午餐"),
        Transaction("收入", 3000, "工资", "七月工资")
    ]

    save_transactions(original_transactions, file_path)

    assert file_path.exists()

    loaded_transactions = load_transactions(file_path)

    assert len(loaded_transactions) == 2

    assert loaded_transactions[0].transaction_type == "支出"
    assert loaded_transactions[0].amount == 25
    assert loaded_transactions[0].category == "餐饮"
    assert loaded_transactions[0].note == "午餐"

    assert loaded_transactions[1].transaction_type == "收入"
    assert loaded_transactions[1].amount == 3000


def test_load_missing_file(tmp_path: Path):
    missing_file = tmp_path / "missing.json"

    transactions = load_transactions(missing_file)

    assert transactions == []