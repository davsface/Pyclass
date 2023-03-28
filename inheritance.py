class Rectangle:
    """
    Represents a geometric rectangle
    """
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * self._length + 2 * self._width


class Square(Rectangle):
    """
    Represents a geometric square
    Inherits from Rectangle
    """
    def __init__(self, side):
        super().__init__(side, side)
    def double_area(self):
        return super().area() * 2

new_square = Square(5)
print(new_square.area())
print(new_square.perimeter())
print(new_square.double_area())