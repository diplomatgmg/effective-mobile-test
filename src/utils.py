import json

from tabulate import tabulate

from src.Record import Record


def validate_selected_record(
    user_choice: str, max_index: int
) -> tuple[int | None, bool]:
    """
    Возвращает record_index, is_error для выбранной записи для редактирования
    """
    try:
        record_index = int(user_choice) - 1
        if record_index < 0 or record_index > max_index:
            raise IndexError
        return record_index, False
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целое число.")
        return None, True
    except IndexError:
        print(
            f"Выбранный номер записи должен быть в диапазоне от 1 до {max_index + 1}."
        )
        return None, True


def print_records(records: list[dict]) -> None:
    """
    Выводит таблицу о всех доходах/расходах пользователя
    """
    json_data = json.loads(json.dumps(records))
    data_with_index = [
        {**{"№": i + 1}, **{k: v for k, v in item.items() if k != "id"}}
        for i, item in enumerate(json_data)
    ]

    print(tabulate(data_with_index, headers="keys", tablefmt="grid"))


def create_record() -> Record:
    """
    Возвращает экземпляр Record на основе введенных данных
    """
    date = input("Введите дату (yyyy-mm-dd или yyyy.mm.dd). Пропуск для текущей даты: ")
    category = input("Введите категорию - Доход/Расход, д/р: ")
    amount = input("Введите сумму: ")
    description = input("Введите описание: ")

    return Record(date, category, amount, description)
