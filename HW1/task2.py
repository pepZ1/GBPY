def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Равносторонний треугольник"
        elif a == b or a == c or b == c:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"
    else:
        return "Треугольник с такими сторонами не существует"

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

result = triangle(a, b, c)
print(result)
