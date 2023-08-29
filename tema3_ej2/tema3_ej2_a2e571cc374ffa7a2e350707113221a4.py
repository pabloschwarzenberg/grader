# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        nsqrd = self.x ** 2 + self.y ** 2 + self.z ** 2
        return nsqrd ** (.5)

    def __add__(self, other):
        r = Vector(0, 0, 0)
        r.x = self.x + other.x
        r.y = self.y + other.y
        r.z = self.z + other.z
        return r

    def __str__(self):
        a = [self.x, self.y, self.z]
        return str(a)

def suma_vectores(v1, v2):
    r = Vector(0, 0, 0)
    r.x = v1.x + v2.x
    r.y = v1.y + v2.y
    r.z = v1.z + v2.z
    return r

