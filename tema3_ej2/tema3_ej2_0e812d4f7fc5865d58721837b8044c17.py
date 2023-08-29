# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return (self.x**2 + self.y**2 + self.z**2)**(1/2)

    def __add__(self, other):
        nuevox = self.x + other.x
        nuevoy = self.y + other.y
        nuevoz = self.z + other.z
        return Vector(nuevox, nuevoy, nuevoz)


def suma_vectores(v1, v2):
    nuevox = v1.x + v2.x
    nuevoy = v1.y + v2.y
    nuevoz = v1.z + v2.z
    return Vector(nuevox,nuevoy,nuevoz)
