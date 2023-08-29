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
            raise TypeError("Operación no válida. Se requiere un objeto de tipo Vector.")

    def __repr__(self):
        return "Vector({0}, {1}, {2})".format(self.x, self.y, self.z)


def suma_vectores(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return v1 + v2
    else:
        raise TypeError("Operación no válida. Se requieren objetos de tipo Vector.")


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print("v1:", v1)
    print("v2:", v2)

    norma_v1 = v1.norma()
    print("Norma de v1:", norma_v1)

    suma = suma_vectores(v1, v2)
    print("Suma de v1 y v2:", suma)
