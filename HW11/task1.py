class Rectangle:
    def __init__(self, height: int, width=None):
        self.height = height
        if width:
            self.width = width
        else:
            self.width = height

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def get_area(self):
        return self.width * self.height

    def __add__(self, other):
        perimeter = self.get_perimeter() + other.get_perimeter()
        side_a = perimeter // 6
        side_b = (perimeter - side_a * 2) // 2

        return Rectangle(side_a, side_b)

    def __sub__(self, other):
        perimeter = abs(self.get_perimeter() - other.get_perimeter())
        side_a = perimeter // 6
        side_b = (perimeter - side_a * 2) // 2

        return Rectangle(side_a, side_b)

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()


spam = Rectangle(1, 9)
eggs = Rectangle(7)

add_reg = spam + eggs
sub_reg = spam - eggs

print(f'{sub_reg.width = }, {sub_reg.height =}')
print(f'{add_reg.width = }, {add_reg.height =}')

print("Are spam and eggs equal in area?", spam == eggs)
print("Is spam's area less than eggs's area?", spam < eggs)
print("Is spam's area less than or equal to eggs's area?", spam <= eggs)
print("Is spam's area greater than eggs's area?", spam > eggs)
print("Is spam's area greater than or equal to eggs's area?", spam >= eggs)
print("Are spam and eggs not equal in area?", spam != eggs)
