import csv
import json
import math
import random

# Функция для нахождения корней квадратного уравнения
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2*a)
        return [x]
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return [x1, x2]

# Функция для генерации CSV файла
def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for _ in range(num_rows):
            row = [random.randint(100, 1000) for _ in range(3)]
            csvwriter.writerow(row)

# Декоратор для выполнения функции с каждой тройкой чисел из CSV файла
def solve_with_csv(func):
    def wrapper(filename):
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                print(f"For coefficients {a}, {b}, {c}: {result}")
    return wrapper

# Декоратор для сохранения параметров и результатов в JSON файл
def save_to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {
            "arguments": args,
            "result": result
        }
        with open('result.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
        return result
    return wrapper

# Пример использования декораторов
@save_to_json
def solve_quadratic_decorated(a, b, c):
    return solve_quadratic(a, b, c)

@solve_with_csv
def solve_quadratic_csv(a, b, c):
    return solve_quadratic(a, b, c)

# Генерация CSV файла
generate_csv('numbers.csv', random.randint(100, 1000))

# Выполнение функции с каждой тройкой чисел из CSV файла
solve_quadratic_csv('numbers.csv')

# Выполнение функции с сохранением параметров и результатов в JSON
solve_quadratic_decorated(1, -3, 2)
