from typing import List, Dict

def group_by_game(table: List[List[str]]) -> Dict[str, Dict[str, List[str]]]:
    """
    Группиовка по названием игр

    table - данные таблицы
    """

    res = {}
    for row in table:
        game_name, character, name_error, _ = row
        if game_name not in res:
            res[game_name] = {}
        if character not in res[game_name]:
            res[game_name][character] = []
        res[game_name][character].append(name_error)

    return res

def log_clear(file_name: str="game_analysis.txt"):
    """
    Очистка лог файла

    file_name - название лог файла
    """

    with open(file_name, "w", encoding="utf-8") as file:
        ...

def log_info_error_by_game(game_name: str, game_info: Dict[str, List[str]], file_name: str="game_analysis.txt"):
    """
    Логирование персанажей с ошибками по играм

    game_name - название игры
    game_info - информация об ошибках у персанажей
    file_name - название лог файла
    """

    total_count = 0
    for v in game_info.values():
        total_count += len(v)
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{game_name}:\n")
        file.write(f"  Total errors: {total_count}\n")  
        for character_name in game_info:
            file.write(f"  {character_name}:\n")
            for error_name in game_info[character_name]:
                file.write(f"   - {error_name}\n")
        file.write("\n\n")

def main() -> None:
    with open("Вариант 11/game.csv", encoding="utf-8") as file:
        table = []
        for i, line in enumerate(file):
            if i == 0:
                continue
            table.append(line.strip('\n').split(","))

    log_clear()

    games = group_by_game(table)
    for game_name, game_info in games.items():
        log_info_error_by_game(game_name, game_info)


if __name__ == '__main__':
    main()
