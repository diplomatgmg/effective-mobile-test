import unittest
from datetime import datetime

from src.Record import Record
from src.exceptions import DateFormatError, CategoryFormatError, AmountFormatError


class TestRecord(unittest.TestCase):

    def test_parse_date(self):
        # Тестирование парсинга даты с правильным форматом
        valid_date_str = "2023-01-01"
        expected_date = datetime.strptime(valid_date_str, "%Y-%m-%d")
        self.assertEqual(Record.parse_date(valid_date_str), expected_date)

        # Тестирование парсинга даты с разделителем "-"
        valid_date_str_hyphen = "2023-01-01"
        self.assertEqual(Record.parse_date(valid_date_str_hyphen), expected_date)

        # Тестирование парсинга даты с разделителем "."
        valid_date_str_dot = "2023.01.01"
        self.assertEqual(Record.parse_date(valid_date_str_dot), expected_date)

        # Тестирование парсинга пустой строки в качестве даты
        self.assertIsInstance(Record.parse_date(""), datetime)

        # Тестирование парсинга неправильного формата даты
        invalid_date_str = "01-01-2023"
        with self.assertRaises(DateFormatError):
            Record.parse_date(invalid_date_str)

    def test_parse_category(self):
        # Тестирование парсинга корректных строк категорий
        valid_income_categories = ["д", "Д", "доход", "Доход"]
        valid_expense_categories = ["р", "Р", "расход", "Расход"]

        for cat in valid_income_categories:
            self.assertEqual(Record.parse_category(cat), "Доход")

        for cat in valid_expense_categories:
            self.assertEqual(Record.parse_category(cat), "Расход")

        # Тестирование парсинга неправильной строки категории
        invalid_category_str = "income"
        with self.assertRaises(CategoryFormatError):
            Record.parse_category(invalid_category_str)

    def test_parse_amount(self):
        # Тестирование парсинга корректных строк суммы
        valid_amount_str_int = "100"
        self.assertEqual(Record.parse_amount(valid_amount_str_int), 100.0)

        valid_amount_str_float = "100.5"
        self.assertEqual(Record.parse_amount(valid_amount_str_float), 100.5)

        # Тестирование парсинга неправильной строки суммы
        invalid_amount_str = "one hundred"
        with self.assertRaises(AmountFormatError):
            Record.parse_amount(invalid_amount_str)

    def test_to_dict(self):
        # Тестирование преобразования объекта Record в словарь
        record = Record("2023-01-01", "доход", "100", "Тестовая запись")
        expected_dict = {
            "id": str(record._id),
            "date": "2023-01-01",
            "category": "Доход",
            "amount": 100.0,
            "description": "Тестовая запись",
        }
        self.assertEqual(record.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
