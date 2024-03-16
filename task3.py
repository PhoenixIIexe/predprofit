from typing import List, Union

def print_game_by_error(games: Union[List[List[str]], List]) -> None:
    """
    Вывод игр с ошибкой

    games - информация об играх
    """

    if games == []:
        print("Этой ошибки не существует")
        return
    for game in games:
        name_error, game_name, character = game
        print(f"Ошибка {name_error} встречается в игре {game_name} у персонажа {character}.")

def find_game_by_error(table: List[List[str]], name_error) -> List[List[str]]:
    """
    Поиск игры по имени ошибки

    table - данные таблицы
    name_error - имя ошибки
    """

    res = []
    for row in table:
        game_name, character, name_error_temp, _ = row
        if name_error_temp == name_error:
            res.append((name_error_temp, game_name, character))

    return res

def main() -> None:
    with open("Вариант 11/game.csv", encoding="utf-8") as file:
        table = []
        for i, line in enumerate(file):
            if i == 0:
                continue
            table.append(line.strip('\n').split(","))

    while True:
        name_error = input("Введите имя ошибки: ")
        if name_error == 'game':
            break
        games = find_game_by_error(table, name_error)
        print_game_by_error(games)




if __name__ == '__main__':
    main()
