class NonNegativeSizeValidator:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("должно быть больше либо равно нулю")
        self.value = value

class Rectangle:
    __slots__ = ('_height', '_width')
    height = NonNegativeSizeValidator()
    width = NonNegativeSizeValidator()

    def __init__(self, height: int, width=None):
        self._height = height
        if width:
            self._width = width
        else:
            self._width = height

    def get_perimeter(self):
        return 2 * (self._height + self._width)

    def get_area(self):
        return self._width * self._height

    def __str__(self):
        return f'прямоугольник ({self._height}x{self._width}), S= {self.get_area()}'

    def __repr__(self):
        return f'размеры:({self._height}x{self._width}), S= {self.get_area()}'

if __name__ == "__main__":
    rect = Rectangle(2, 5)
    rect.width = 0

    print(rect)
