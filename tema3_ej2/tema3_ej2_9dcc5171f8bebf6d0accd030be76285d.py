class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            x_sum = self.x + other.x
            y_sum = self.y + other.y
            z_sum = self.z + other.z
            return Vector(x_sum, y_sum, z_sum)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Vector' and '{}'".format(type(other).__name__))


def suma_vectores(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return v1 + v2
    else:
        raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(type(v1).__name__, type(v2).__name__))
