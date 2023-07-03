number = int(input("Введите число от 1 до 999: "))


if 1 <= number <= 9:
    square = number ** 2
    print("Введена цифра. Квадрат числа:", square)
elif 10 <= number <= 99:
    digit1 = number // 10
    digit2 = number % 10
    product = digit1 * digit2
    print("Введено двузначное число. Произведение цифр:", product)
elif 100 <= number <= 999:
    digit3 = number % 10
    digit2 = (number // 10) % 10
    digit1 = number // 100
    reversed_number = digit3 * 100 + digit2 * 10 + digit1
    print("Введено трёхзначное число. Зеркальное отображение:", reversed_number)
else:
    print("Число вне диапазона. Пожалуйста, введите новое число.")