import numbers


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def component_division(self, divisor):
        return Vector2(self.x / divisor.x, self.y / divisor.y)

    def component_multiplication(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        raise TypeError(f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")

    def __sub__(self, other):
        return self + other * -1

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Vector2(self.x * other, self.y * other)
        raise TypeError(f"unsupported operand type(s) for *: '{type(self)}' and '{type(other)}'")

    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            return Vector2(self.x / other, self.y / other)
        raise TypeError(f"unsupported operand type(s) for /: '{type(self)}' and '{type(other)}'")

    def __iter__(self):
        return iter([self.x, self.y])

    def __str__(self):
        return f"Vector2({self.x}, {self.y})"
    
    def __repr__(self):
        return str(self)

