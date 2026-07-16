import csv
import json
from pathlib import Path

from app.models import Transaction


def save_transactions(
    transactions: list[Transaction],
    file_path: Path
) -> None:
    data = [
        transaction.to_dict()
        for transaction in transactions
    ]

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )

    print("数据保存成功：", file_path)


def load_transactions(
    file_path: Path
) -> list[Transaction]:
    if not file_path.exists():
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [
            Transaction.from_dict(item)
            for item in data
        ]

    except (
        json.JSONDecodeError,
        KeyError,
        TypeError,
        ValueError
    ) as error:
        print("数据读取失败：", error)
        return []


def export_csv(
    transactions: list[Transaction],
    file_path: Path
) -> None:
    fieldnames = [
        "transaction_type",
        "amount",
        "category",
        "note"
    ]

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        file_path,
        "w",
        encoding="utf-8-sig",
        newline=""
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(
            transaction.to_dict()
            for transaction in transactions
        )

    print("CSV导出成功：", file_path)