# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        x = self.x
        y = self.y
        z = self.z
        norma_vector = ((x ** 2) + (y ** 2) + (z ** 2)) ** 0.5
        return norma_vector

    def __add__(self, other):
        v3 = suma_vectores(self, other)
        return v3



def suma_vectores(v1, v2):
    v3_x = v1.x + v2.x
    v3_y = v1.y + v2.y
    v3_z = v1.z + v2.z
    v3 = Vector(v3_x, v3_y, v3_z)
    print(type(v3))
    return v3




           