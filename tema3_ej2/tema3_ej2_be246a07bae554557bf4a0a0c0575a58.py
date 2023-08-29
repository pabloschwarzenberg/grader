import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            new_z = self.z + other.z
            return Vector(new_x, new_y, new_z)
        else:
            raise TypeError("Invalid operand type. Operand must be a Vector object.")

def suma_vectores(a, b):
    if isinstance(a, Vector) and isinstance(b, Vector):
        return a + b
    else:
        raise TypeError("Invalid operand types. Operands must be Vector objects.")


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print(f"Norma de v1: {v1.norma()}")
    print(f"Norma de v2: {v2.norma()}")

    v3 = suma_vectores(v1, v2)
    print(f"Suma de v1 y v2: ({v3.x}, {v3.y}, {v3.z})")

    v4 = v1 + v2
    print(f"Suma de v1 y v2: ({v4.x}, {v4.y}, {v4.z})")
