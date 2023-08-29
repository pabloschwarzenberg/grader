import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Unsupported operand type for +")

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


def suma_vectores(v1, v2):
    return v1 + v2


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = suma_vectores(v1, v2)
    print(v1.norma())  # 3.7416573867739413
    print(v2.norma())  # 8.774964387392123
    print(v3)  # Vector(5, 7, 9)