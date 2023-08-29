# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("El objeto no es de tipo Vector")


def suma_vectores(v1, v2):
    return v1 + v2


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = suma_vectores(v1, v2)

    print("v1 =", v1.x, v1.y, v1.z)
    print("v2 =", v2.x, v2.y, v2.z)
    print("v3 =", v3.x, v3.y, v3.z)
    print("Norma v1 =", v1.norma())
    print("Norma v2 =", v2.norma())
    print("Norma v3 =", v3.norma())
