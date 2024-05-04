from src.Wallet import Wallet
from src.Record import Record


def main():
    """
    Инициализирует изначальный кошелек пользователя.
    Файл с БД хранится в той же директории, что и settings.py
    Файл с БД от кошелька передаётся в аргументы Wallet(filename=...)
    filename по умолчанию - db.
    """
    wallet = Wallet()
    wallet.load_data()
    print(wallet)

    while True:
        print("\n1. Вывести баланс")
        print("2. Добавление записи")
        print("0. Выход")

        choice = input("\nВыберите действие: ")

        match choice.strip():
            case "1":
                income = wallet.get_balance("Доход")
                expenses = wallet.get_balance("Расход")
                difference = round(income - expenses, 2)
                # Добавляем "+" для положительного баланса для читаемости
                prefix = "+" if difference > 0 else ""

                print(f"Суммарный доход: {"{:.2f}".format(income)}")
                print(f"Всего потрачено: {"{:.2f}".format(expenses)}")
                print(f"Разница: {prefix}{"{:.2f}".format(difference)}")

            case "2":
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
