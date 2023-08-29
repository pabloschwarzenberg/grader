# crea la clase Vector y completa el código de la función suma_vectores usándola
def suma_vectores(v1,v2):
  return
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
            raise TypeError("La suma solo puede realizarse entre objetos de tipo Vector")

def suma_vectores(v1, v2):
    return v1 + v2
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

v3 = suma_vectores(v1, v2)
print("Suma de vectores:", v3.x, v3.y, v3.z)

norma_v1 = v1.norma()
print("Norma de v1:", norma_v1)
           