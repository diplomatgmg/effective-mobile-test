import unittest
import os

from src.Record import Record
from src.Wallet import Wallet
from src.settings import BASE_DIR


class TestWallet(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet("test_db")

    def tearDown(self):
        if os.path.exists(BASE_DIR / "test_db.json"):
            os.remove(BASE_DIR / "test_db.json")

    def test_init(self):
        # Проверка инициализации объекта
        self.assertEqual(self.wallet.filename, "test_db")
        # self.assertEqual(self.wallet.records, [])

    def test_get_db_file(self):
        # Проверка получения пути к файлу БД
        expected_path = os.path.join(BASE_DIR, "test_db.json")
        self.assertEqual(self.wallet.get_db_file(), expected_path)

    def test_load_data(self):
        # Создание образцовой записи и ее сохранение
        record = Record("2023-01-01", "доход", "100", "Тестовая запись")
        self.wallet.add_record(record)
        self.wallet.save_records()

        # Загрузка данных и проверка наличия записи
        self.wallet.load_data()
        self.assertEqual(len(self.wallet.records), 2)
        loaded_record = self.wallet.records[0]
        self.assertEqual(loaded_record.date, record.date)
        self.assertEqual(loaded_record.category, record.category)
        self.assertEqual(loaded_record.amount, record.amount)
        self.assertEqual(loaded_record.description, record.description)

    def test_save_records(self):
        # Создание образцовой записи и добавление ее
        record = Record("2023-01-01", "доход", "100", "Тестовая запись")
        self.wallet.add_record(record)

        # Сохранение записей и проверка наличия файла
        self.wallet.save_records()
        self.assertTrue(os.path.exists(BASE_DIR / "test_db.json"))

    def test_add_record(self):
        # Добавление образцовой записи
        record = Record("2023-01-01", "доход", "100", "Тестовая запись")
        self.wallet.add_record(record)

        # Проверка добавления записи
        self.assertEqual(len(self.wallet.records), 1)
        added_record = self.wallet.records[0]
        self.assertEqual(added_record.date, record.date)
        self.assertEqual(added_record.category, record.category)
        self.assertEqual(added_record.amount, record.amount)
        self.assertEqual(added_record.description, record.description)

    def test_edit_record(self):
        # Добавление образцовой записи
        record = Record("2023-01-01", "доход", "100", "Тестовая запись")
        self.wallet.add_record(record)

        # Изменение записи
        edited_record = Record("2023-01-02", "расход", "50", "Измененная запись")
        self.wallet.edit_record(0, edited_record)

        # Проверка изменения записи
        self.assertEqual(len(self.wallet.records), 1)
        edited_record_check = self.wallet.records[0]
        self.assertEqual(edited_record_check.date, edited_record.date)
        self.assertEqual(edited_record_check.category, edited_record.category)
        self.assertEqual(edited_record_check.amount, edited_record.amount)
        self.assertEqual(edited_record_check.description, edited_record.description)

    def test_get_balance(self):
        # Добавление образцовых записей
        records = [
            Record("2023-01-01", "доход", "100", "Доход 1"),
            Record("2023-01-02", "доход", "200", "Доход 2"),
            Record("2023-01-03", "расход", "50", "Расход 1"),
            Record("2023-01-04", "расход", "70", "Расход 2"),
        ]
        for record in records:
            self.wallet.add_record(record)

        # Проверка баланса по доходам и расходам
        self.assertEqual(self.wallet.get_balance("доход"), 300.0)
        self.assertEqual(self.wallet.get_balance("расход"), 120.0)

    def test_search_records(self):
        # Добавление образцовых записей
        records = [
            Record("2023-01-01", "доход", "100", "Доход 1"),
            Record("2023-01-02", "доход", "200", "Доход 2"),
            Record("2023-01-03", "расход", "50", "Расход 1"),
            Record("2023-01-04", "расход", "70", "Расход 2"),
        ]
        for record in records:
            self.wallet.add_record(record)

        # Поиск записей
        search_result = self.wallet.search_records("Доход")
        self.assertEqual(len(search_result), 2)
        self.assertEqual(search_result[0].description, "Доход 1")
        self.assertEqual(search_result[1].description, "Доход 2")


if __name__ == "__main__":
    unittest.main()
