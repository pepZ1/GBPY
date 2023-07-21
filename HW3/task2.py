def fill_backpack(items, max_weight):
    # Сортируем список вещей по возрастанию массы
    sorted_items = sorted(items, key=lambda x: x[1])

    backpack_contents = []
    current_weight = 0

    for item in sorted_items:
        # Если добавление вещи не превышает максимальную грузоподъемность, добавляем ее в рюкзак
        if current_weight + item[1] <= max_weight:
            backpack_contents.append(item[0])
            current_weight += item[1]

    return backpack_contents


things = {
    "Тент": 2,
    "Спальник": 3,
    "Фонарик": 1,
    "Еда": 4,
    "Палатка": 5,
    "Вода": 2,
}

max_backpack_weight = 10
result = fill_backpack(list(things.items()), max_backpack_weight)
print("Вещи в рюкзаке:")
print(result)