import uuid
from datetime import datetime
from typing import Union

TCategory = Union["Доход", "Расход"]


class Record:
    """
    Класс для представления одной записи о доходе/расходе
    """

    id: uuid.UUID
    date: datetime
    category: TCategory
    amount: int
    description: str

    def __init__(
        self,
        date: datetime,
        category: TCategory,
        amount: int,
        description: str,
    ):
        self.id = uuid.uuid4()
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"id: {self.id}"
