class Transaction:
    def __init__(
        self,
        transaction_type: str,
        amount: float,
        category: str,
        note: str
    ) -> None:
        self.transaction_type = transaction_type
        self.amount = amount
        self.category = category
        self.note = note

    def show(self) -> None:
        print(f"{self.transaction_type}：{self.amount:.2f}元")
        print(f"分类：{self.category}")
        print(f"备注：{self.note}")

    def to_dict(self) -> dict[str, object]:
        return {
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "category": self.category,
            "note": self.note
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, object]
    ) -> "Transaction":
        return cls(
            transaction_type=str(data["transaction_type"]),
            amount=float(data["amount"]),
            category=str(data["category"]),
            note=str(data["note"])
        )