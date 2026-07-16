from pathlib import Path

from app.models import Transaction
from app.storage import (
    export_csv,
    load_transactions,
    save_transactions
)


project_folder = Path(__file__).parent.parent
data_file = project_folder / "data" / "transactions.json"
csv_file = project_folder / "exports" / "transactions.csv"

data_file.parent.mkdir(parents=True, exist_ok=True)
csv_file.parent.mkdir(parents=True, exist_ok=True)

transactions = load_transactions(data_file)

new_transaction = Transaction(
    "支出",
    25,
    "餐饮",
    "午餐"
)

transactions.append(new_transaction)

save_transactions(transactions, data_file)
export_csv(transactions, csv_file)

for transaction in transactions:
    transaction.show()
    print("--------------------")
total_income = sum(
    transaction.amount
    for transaction in transactions
    if transaction.transaction_type == "收入"
)

total_expense = sum(
    transaction.amount
    for transaction in transactions
    if transaction.transaction_type == "支出"
)

balance = total_income - total_expense

print(f"总收入：{total_income:.2f}元")
print(f"总支出：{total_expense:.2f}元")
print(f"当前余额：{balance:.2f}元")