import re
import uuid
from datetime import datetime

from src.exceptions import CategoryFormatError, DateFormatError, AmountFormatError


class Record:
    """
    Класс для представления одной записи о доходе/расходе
    """

    _id: uuid.UUID
    date: datetime
    category: str
    amount: float
    description: str

    def __init__(
        self,
        date: str,
        category: str,
        amount: str,
        description: str,
        _id=None,
    ):
        self._id = uuid.UUID(_id) if _id else uuid.uuid4()
        self.date = self.parse_date(date)
        self.category = self.parse_category(category)
        self.amount = self.parse_amount(amount)
        self.description = description.strip()

    def __str__(self):
        return f"Record id: {self._id}"

    @staticmethod
    def parse_date(date: str = "") -> datetime:
        """
        Преобразует дату в удобный формат.
        Если на вход поступает пустая строка, используется текущая дата.
        """
        date_format = "%Y%m%d"

        if not date.strip():
            return datetime.now()

        match = re.search(r"\d{4}[-.]\d{2}[-.]\d{2}\b", date.strip())

        if match:
            date_str = match.group().replace("-", "").replace(".", "")
            return datetime.strptime(date_str, date_format)
        else:
            raise DateFormatError(
                "Неизвестный формат даты. Ожидалось: yyyy-mm-dd или yyyy.mm.dd"
            )

    @staticmethod
    def parse_category(category: str) -> str:
        """
        Преобразует категорию в удобный формат
        """
        match category.strip().lower():
            case "д" | "доход":
                return "Доход"
            case "р" | "расход":
                return "Расход"
            case _:
                raise CategoryFormatError(
                    "Неизвестный формат категории. Ожидалось: Доход/Расход, д/р"
                )

    @staticmethod
    def parse_amount(amount: str) -> float:
        """
        Преобразует сумму в удобный формат
        """
        try:
            return float(amount)
        except ValueError:
            raise AmountFormatError(
                "Неизвестный формат суммы. Ожидалось: целое/вещественное число"
            )

    def to_dict(self) -> dict:
        """
        Преобразует поля из класса в удобный формат для json
        """
        return {
            "id": str(self._id),
            "date": self.date.strftime("%Y-%m-%d"),
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
        }
