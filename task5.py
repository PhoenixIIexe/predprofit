from typing import List, Dict, Tuple
from datetime import datetime

def log_clear(file_name: str="error.txt"):
    """
    Очистка лог файла

    file_name - название лог файла
    """

    with open(file_name, "w", encoding="utf-8") as file:
        ...

def log_date_errors(date: str, errors: List[str], first: bool=False, file_name: str="error.txt"):
    """
    Логирование персанажей с ошибками по играм

    date - дата
    errors - ошибки в эту дату
    first - первая ли это ошибка
    file_name - название лог файла
    """

    with open(file_name, "a", encoding="utf-8") as file:
        if first:
            file.write("Список ошибок по датам:\n")
        file.write(f"{date}: {', '.join(errors)}\n")

def group_by_error(table: List[List[str]]) -> Dict[str, List[Tuple[str]]]:
    """
    Группировка по именам ошибки

    table - данные таблицы
    """

    res = {}
    for row in table:
        game_name, character, name_error, _ = row
        if name_error not in res:
            res[name_error] = []
        res[name_error].append((game_name, character))

    return res

def error_by_date(table: List[List[str]]) -> Dict[str, List[Tuple[str]]]:
    """
    Группировка ошибок по дате

    table - данные таблицы
    """

    res = {}
    for row in table:
        *_, name_error, date = row
        if date not in res:
            res[date] = []
        res[date].append(name_error)

    return res

def print_game_with_error(table: List[List[str]]) -> None:
    """
    Вывод всех игр с ошибками

    table - данные таблицы
    """

    used = set()
    
    print("Игры с ошибками:")
    for row in table:
        game_name, *_ = row
        if game_name not in used:
            print(game_name)
            used.add(game_name)


def main() -> None:
    with open("Вариант 11/game.csv", encoding="utf-8") as file:
        table = []
        for i, line in enumerate(file):
            if i == 0:
                continue
            table.append(line.strip('\n').split(","))

    table_by_error = group_by_error(table)
    print_game_with_error(table)
    dates_errors = error_by_date(table)

    log_clear()
    first = True
    for date in sorted(dates_errors, key=lambda date: datetime.strptime(date, "%Y-%m-%d")):
        log_date_errors(date, dates_errors[date], first)
        first = False
    

if __name__ == '__main__':
    main()
