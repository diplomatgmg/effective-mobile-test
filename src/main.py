from src.Wallet import Wallet
from src.Record import Record


def main():
    """
    Инициализирует изначальный кошелек пользователя.
    Файл с БД хранится в той же директории, что и settings.py
    Файл с БД от кошелька передаются в аргументы Wallet(filename=...)
    filename по умолчанию - db.json.
    """
    wallet = Wallet()
    wallet.load_data()
    print(wallet)

    while True:
        print("1. Добавление записи")
        print("0. Выход")

        choice = input("Выберите действие: ")

        match choice.strip():
            case "1":
                date = input(
                    "Введите дату (yyyy-mm-dd или yyyy.mm.dd). Пропуск для текущей даты: "
                )
                category = input("Введите категорию - Доход/Расход, д/р: ")
                amount = input("Введите сумму: ")
                description = input("Введите описание: ")

                record = Record(date, category, amount, description)
                wallet.add_record(record)
                print(wallet)
            case "0":
                print("\nВсе данные сохранены. Выход")
                break
            case _:
                print("\nНеизвестное действие. Повторите попытку")


if __name__ == "__main__":
    main()
