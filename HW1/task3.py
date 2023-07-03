number = int(input("Введите число: "))

if number < 0 or number > 100000:
    print("Число должно быть положительным и не превышать 100 тысяч.")
else:
    is_prime = True

    if number < 2:
        is_prime = False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Число является простым.")
    else:
        print("Число является составным.")