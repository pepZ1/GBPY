def find_common_items(friends_items):
    common_items = set(friends_items[0])

    for items in friends_items[1:]:
        common_items &= set(items)

    return common_items

def find_unique_items(friends_items):
    all_items = set().union(*friends_items)

    unique_items = [all_items - set(items) for items in friends_items]

    return unique_items

def find_items_except_one(friends_items):
    result = {}

    all_items = set().union(*friends_items)

    for friend, items in zip(friends, friends_items):
        items_except_one = all_items - set(items)
        result[friend] = items_except_one

    return result

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