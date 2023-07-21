def remove_duplicates(input_list):
    unique_set = set(input_list)

    unique_list = list(unique_set)

    return unique_list

duplicated_list = [1, 2, 2, 3, 4, 4, 4, 5]
result_list = remove_duplicates(duplicated_list)
print("список без дубликатов:", result_list)