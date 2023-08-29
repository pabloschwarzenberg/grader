import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    @staticmethod
    def suma_vectores(v1, v2):
        x = v1.x + v2.x
        y = v1.y + v2.y
        z = v1.z + v2.z
        return Vector(x, y, z)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    # Uso del método norma
    print("Norma de v1:", v1.norma())
    print("Norma de v2:", v2.norma())

    # Uso de la función suma_vectores
    v3 = Vector.suma_vectores(v1, v2)
    print("Suma de v1 y v2:", v3.x, v3.y, v3.z)

    # Uso de la sobrecarga del operador +
    v4 = v1 + v2
    print("Suma de v1 y v2:", v4.x, v4.y, v4.z)
           