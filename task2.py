from typing import Iterable
import random


def partition(a: Iterable, l: int, r: int, pivot: int) -> None:
    """
    Измение значение на полуинтервали относительно заданного значения

    a - сортируемая последовательность
    l - левая граница
    r - правая граница
    pivot - значение относительно, которого происходит сортировка
    """

    i = l
    j = r - 1
    while i <= j:
        while a[i][1] < pivot:
            i += 1
        while a[j][1] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    return i

def quick_sort(a: Iterable, l: int, r: int) -> None:
    """
    Быстрая сортировка последовательности

    a - сортируемая последовательность
    l - левая граница
    r - правая граница
    """

    if r - l <= 1:
        return
    
    pivot = a[random.randint(l, r - 1)][1]
    p = partition(a, l, r, pivot)
    quick_sort(a, l, p)
    quick_sort(a, p, r)

def print_bug_character(character: str, count_bug: str) -> None:
    """
    Вывод информации о багах

    character - имя персонажа
    count_bug - количество багов
    """

    print(f"{character} - количество багов: {count_bug}")

def main() -> None:
    with open("Вариант 11/game.csv", encoding="utf-8") as file:
        table = []
        for i, line in enumerate(file):
            if i == 0:
                continue
            table.append(line.strip('\n').split(","))

    quick_sort(table, 0, len(table))
    count_bug = -1
    last_character = ""
    for row in table:
        _, character, *_ = row
        if character != last_character and count_bug != -1:
            print_bug_character(last_character, count_bug)
            count_bug = 0
        last_character = character
        count_bug += 1
    print_bug_character(last_character, count_bug)


if __name__ == '__main__':
    main()
