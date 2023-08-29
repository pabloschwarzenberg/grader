# crea la clase Vector y completa el código de la función suma_vectores usándola
def suma_vectores(v1,v2):
  return
import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def norma(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            new_z = self.z + other.z
            return Vector(new_x, new_y, new_z)
        else:
            raise TypeError("El objeto pasado como parámetro no es de tipo Vector.")

# Función suma_vectores
def suma_vectores(vector1, vector2):
    return vector1 + vector2

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

norma_v1 = v1.norma()
print("Norma del vector v1:", norma_v1)

v3 = suma_vectores(v1, v2)
print("Suma de v1 y v2:", v3.x, v3.y, v3.z)

v4 = v1 + v2
print("Suma de v1 y v2 (usando sobrecarga del operador +):", v4.x, v4.y, v4.z)
