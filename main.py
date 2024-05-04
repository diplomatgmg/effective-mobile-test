from src.Wallet import Wallet

from src.utils import validate_selected_record, print_records, create_record


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
        print("3. Редактирование записи")
        print("4. Поиск записей")
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
                record = create_record()
                wallet.add_record(record)
                print(wallet)

            case "3":
                records = [record.to_dict() for record in wallet.records]

                if len(records) == 0:
                    print("У вас нет записей. Изменять нечего.")
                    continue

                print_records(records)

                while True:
                    user_choice = input("Выберите номер нужной записи. Выход - 0: ")

                    if user_choice.strip() == "0":
                        break

                    record_index, is_error = validate_selected_record(
                        user_choice, max_index=len(records) - 1
                    )

                    if is_error:
                        continue

                    record = create_record()
                    wallet.edit_record(record_index, record)
                    break

            case "4":
                query = input("Введите текст для поиска: ").strip()
                results = wallet.search_records(query)

                if results:
                    results_data = [record.to_dict() for record in results]
                    print("Найденные записи:")
                    print_records(results_data)
                else:
                    print("Ничего не найдено.")

            case "0":
                print("\nВсе данные сохранены. Выход")
                break
            case _:
                print("\nНеизвестное действие. Повторите попытку")


if __name__ == "__main__":
    main()
