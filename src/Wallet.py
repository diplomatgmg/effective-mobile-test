import json

from src.Record import Record
from src.settings import DATABASE_FILENAME, BASE_DIR


class Wallet:
    """
    Класс для управления доходами/расходами пользователя
    """

    filename: str
    records: list[Record]

    def __init__(self, filename=None):
        self.filename = filename or DATABASE_FILENAME
        self.records = []

    def __str__(self):
        return f"Файл БД: {self.get_db_file()}\nЗаписей: {len(self.records)}"

    def get_db_file(self):
        """
        Возвращает полный путь до файла БД
        """
        return BASE_DIR / (self.filename + ".json")

    def load_data(self):
        """
        Парсит файл с БД и добавляет данные о платежах в Wallet
        """
        try:
            with open(self.get_db_file(), "r", encoding="utf8") as file:
                data = json.load(file)
                for json_record in data:
                    json_record["_id"] = json_record.pop("id")
                    record = Record(**json_record)
                    self.records.append(record)
        except FileNotFoundError:
            pass

    def save_records(self):
        """
        Получает все данные о платежах пользователя и сохраняет в БД
        """
        data = [record.to_dict() for record in self.records]
        with open(self.get_db_file(), "w", encoding="utf8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_record(self, record):
        """
        Добавляет данные о платежах в Wallet и сохраняет данные в БД
        """
        self.records.append(record)
        self.save_records()
