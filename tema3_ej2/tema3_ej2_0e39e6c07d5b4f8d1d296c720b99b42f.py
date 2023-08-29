class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return ((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) ** 0.5

    def __add__(self, operando):
        nx = self.x + operando.x

        ny = self.y + operando.y

        nz = self.z + operando.z
        return Vector(nx, ny, nz)


def suma_vectores(a, b):
    c = a + b
    return c












