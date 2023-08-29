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
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Invalid operand type. Only Vector objects can be added.")
    
def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1 + vector2
    else:
        raise TypeError("Invalid operand types. Both parameters must be Vector objects.")

# Ejemplo de uso:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Norma de v1:", v1.norma())  # Resultado: 3.7416573867739413

v3 = suma_vectores(v1, v2)
print("Suma de v1 y v2:", v3.x, v3.y, v3.z)  # Resultado: 5, 7, 9

v4 = v1 + v2
print("Suma de v1 y v2 (usando operador +):", v4.x, v4.y, v4.z)  # Resultado: 5, 7, 9
