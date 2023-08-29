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
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            return Vector(x, y, z)
        else:
            raise TypeError("Operación no válida. Los operandos deben ser de tipo Vector.")

def suma_vectores(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return v1 + v2
    else:
        raise TypeError("Operación no válida. Los operandos deben ser de tipo Vector.")

if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print("Vector v1:", v1.x, v1.y, v1.z)
    print("Vector v2:", v2.x, v2.y, v2.z)

    norma_v1 = v1.norma()
    print("Norma del vector v1:", norma_v1)

    v3 = suma_vectores(v1, v2)
    print("Resultado de la suma de v1 y v2:", v3.x, v3.y, v3.z)
