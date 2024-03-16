from typing import List

def log_clear(file_name: str="game_new.txt") -> None:
    """
    Очистка лог файла

    file_name - Название лог файла
    """

    with open(file_name, "w", encoding="utf-8") as file:
        ...

def log_character(row: List[str], file_name: str="game_new.txt") -> None:
    """
    Запусти ошибок у персанажей в лог файл

    row - Информация о персанаже
    file_name - Название лог файла
    """

    with open(file_name, "a", encoding="utf-8") as file:
        game_name, character, name_error, date = row
        file.write(f"У персонажа {character} в игре {game_name} нашлась ошибка с кодом: {name_error}. Дата фиксации: {date}.\n")

def main() -> None:
    with open("Вариант 11/game.csv", encoding="utf-8") as file:
        table = []
        for i, line in enumerate(file):
            if i == 0:
                continue
            table.append(line.strip('\n').split(","))

    log_clear()

    first_game = ""
    for row in table:
        game_name, character, *_ = row
        if character == 'Avery':
            log_character(row)
            if first_game == "":
                first_game = game_name

    print(first_game)


if __name__ == '__main__':
    main()
