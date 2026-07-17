from pathlib import Path

from app.models import Transaction
from app.storage import (
    export_csv,
    load_transactions,
    save_transactions,
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "transactions.json"
CSV_FILE = BASE_DIR / "exports" / "transactions.csv"


def show_menu() -> None:
    print("\n===== 个人记账系统 =====")
    print("1. 添加交易")
    print("2. 查看全部交易")
    print("3. 查看收支汇总")
    print("4. 导出CSV")
    print("0. 退出程序")


def show_transactions(transactions: list[Transaction]) -> None:
    if not transactions:
        print("目前没有交易记录")
        return

    print("\n===== 全部交易记录 =====")

    for index, transaction in enumerate(transactions, start=1):
        print(f"\n第{index}条记录")
        transaction.show()
        print("--------------------")
def add_transaction(
    transactions: list[Transaction]
) -> None:
    while True:
        transaction_type = input(
            "请输入交易类型（收入/支出）："
        ).strip()

        if transaction_type in ["收入", "支出"]:
            break

        print("交易类型只能输入“收入”或“支出”")

    while True:
        amount_text = input("请输入金额：").strip()

        try:
            amount = float(amount_text)

            if amount <= 0:
                print("金额必须大于0")
                continue

            break

        except ValueError:
            print("金额格式错误，请输入数字")

    while True:
        category = input("请输入分类：").strip()

        if category:
            break

        print("分类不能为空")

    note = input("请输入备注：").strip()

    if not note:
        note = "无"

    new_transaction = Transaction(
        transaction_type,
        amount,
        category,
        note
    )

    transactions.append(new_transaction)

    save_transactions(transactions, DATA_FILE)

    print("交易添加成功")

def show_summary(
    transactions: list[Transaction]
) -> None:
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

    print("\n===== 收支汇总 =====")
    print(f"总收入：{total_income:.2f}元")
    print(f"总支出：{total_expense:.2f}元")
    print(f"当前余额：{balance:.2f}元")

def main() -> None:
    transactions = load_transactions(DATA_FILE)

    while True:
        show_menu()

        choice = input("请选择操作：").strip()

        if choice == "1":
            add_transaction(transactions)

        elif choice == "2":
            show_transactions(transactions)

        elif choice == "3":
            show_summary(transactions)

        elif choice == "4":
            export_csv(transactions, CSV_FILE)

        elif choice == "0":
            print("程序已退出")
            break

        else:
            print("输入无效，请输入0到4之间的数字")


if __name__ == "__main__":
    main()