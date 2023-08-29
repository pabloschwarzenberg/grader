# crea la clase Vector y completa el código de la función suma_vectores usándola
def suma_vectores(v1,v2):
  return
 import math

class Vector:
    def _init_(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x*2 + self.y2 + self.z*2)

    def _add_(self, other):
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            return Vector(x, y, z)
        else:
            raise ValueError("La operación de suma solo es válida para objetos de la clase Vector.")

    def _repr_(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)


def suma_vectores(vector1, vector2):
    return vector1 + vector2


# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Calcular la norma del vector v1
print("Norma de v1:", v1.norma())

# Sumar dos vectores
v3 = suma_vectores(v1, v2)
print("Suma de v1 y v2:", v3)

# Usar el operador + para sumar dos vectores
v4 = v1 + v2
print("Suma de v1 y v2 (con operador +):", v4)          