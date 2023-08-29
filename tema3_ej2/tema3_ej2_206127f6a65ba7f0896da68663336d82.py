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
            x_sum = self.x + other.x
            y_sum = self.y + other.y
            z_sum = self.z + other.z
            return Vector(x_sum, y_sum, z_sum)
        else:
            raise TypeError("El operando no es un objeto de la clase Vector.")

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1 + vector2
    else:
        raise TypeError("Los operandos no son objetos de la clase Vector.")


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print("Norma del vector v1:", v1.norma())
    print("Norma del vector v2:", v2.norma())

    v3 = suma_vectores(v1, v2)
    print("Suma de v1 y v2:", v3)
