import functools

def run_multiple_times(num_runs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(num_runs):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator


@run_multiple_times(num_runs=5)
def square_number(number):
    return number ** 2

result = square_number(3)
print(result)  # Вывод: [9, 9, 9, 9, 9]
