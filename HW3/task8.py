def find_common_items(friends_items):
    # Создаем множество из вещей первого друга
    common_items = set(friends_items[0])

    # Находим пересечение множеств вещей всех друзей
    for items in friends_items[1:]:
        common_items &= set(items)

    return common_items

def find_unique_items(friends_items):
    # Создаем объединение множеств вещей всех друзей
    all_items = set().union(*friends_items)

    # Находим разницу множеств вещей каждого друга и всего объединенного множества
    unique_items = [all_items - set(items) for items in friends_items]

    return unique_items

def find_items_except_one(friends_items):
    result = {}

    # Создаем объединение множеств вещей всех друзей
    all_items = set().union(*friends_items)

    # Находим разницу множеств вещей каждого друга и всего объединенного множества
    for friend, items in zip(friends, friends_items):
        items_except_one = all_items - set(items)
        result[friend] = items_except_one

    return result

# Пример использования
friends = ["Друг 1", "Друг 2", "Друг 3"]
friends_items = [
    ["Тент", "Спальник", "Фонарик", "Еда"],
    ["Тент", "Фонарик", "Вода"],
    ["Тент", "Спальник", "Фонарик", "Еда", "Палатка"],
]

common_items = find_common_items(friends_items)
print("Вещи, которые взяли все три друга:", common_items)

unique_items = find_unique_items(friends_items)
print("Уникальные вещи, есть только у одного друга:", unique_items)

items_except_one = find_items_except_one(friends_items)
print("Вещи, которые есть у всех друзей кроме одного:")
for friend, items in items_except_one.items():
    print(f"{friend}: {items}")