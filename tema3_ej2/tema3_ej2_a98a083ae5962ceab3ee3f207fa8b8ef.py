# crea la clase Vector y completa el código de la función suma_vectores usándola
# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        a = (self.x) ** 2
        b = (self.y) ** 2
        c = (self.z) ** 2
        return ((a + b + c) ** (1 / 2))

    def __add__(self, other):
        q = self.x + other.x
        w = self.y + other.y
        e = self.z + other.z
        return Vector(q, w, e)


def suma_vectores(v1, v2):
    ve3=v1+v2
    return ve3


ve1 = Vector(1, 2, 3)
ve2 = Vector(2, 3, 4)

ve3 = suma_vectores(ve1, ve2)
print(ve3.x)
print(ve3.y)
print(ve3.z)