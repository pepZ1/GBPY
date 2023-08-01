# ------------------------------------------- 2 -----------------------------
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.

# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 -
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# ------------------------------------------- 3 -----------------------------
# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел
# для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
import itertools
import random


def are_queens_attacking_each_other(queens_positions):
    """
    Функция для проверки, атакуют ли ферзи друг друга.

    Args:
        queens_positions (list): Список, содержащий координаты ферзей на доске в формате (строка, столбец).

    Returns:
        bool: True, если ферзи не атакуют друг друга, иначе False.
    """

    # Проверяем, атакуют ли ферзи друг друга на доске.
    # Для этого перебираем все возможные пары ферзей.
    for i in range(len(queens_positions)):
        for j in range(i + 1, len(queens_positions)):
            row1, col1 = queens_positions[i]
            row2, col2 = queens_positions[j]

            # Проверяем, находятся ли ферзи на одной горизонтали, вертикали или диагонали
            if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
                return False
    return True


def generate_successful_arrangements():
    """
    Функция для генерации 4 успешных расстановок ферзей на доске.

    Returns:
        list: Список с 4 успешными расстановками ферзей.
    """
    successful_args = []

    # Генерируем все возможные перестановки чисел от 1 до 8
    all_permutations = list(itertools.permutations(range(1, 9)))

    # Перемешиваем порядок перестановок для случайности
    random.shuffle(all_permutations)

    for permutation in all_permutations:
        # Преобразуем перестановку в список позиций ферзей в формате (строка, столбец)
        queens_positions = [(i + 1, permutation[i]) for i in range(8)]

        # Проверяем, атакуют ли ферзи друг друга
        if are_queens_attacking_each_other(queens_positions):
            # Если расстановка успешна, добавляем ее в список
            successful_args.append(queens_positions)

            # Если уже нашли 4 успешные расстановки, завершаем цикл
            if len(successful_args) == 4:
                break

    return successful_args


# Генерируем и выводим 4 успешные расстановки ферзей
successful_arrangements = generate_successful_arrangements()

print("УСПЕШНЫЕ РАССТАНОВКИ ФЕРЗЕЙ:")
for i, arrangement in enumerate(successful_arrangements, 1):
    print(f"Расстановка {i}: {arrangement}")
