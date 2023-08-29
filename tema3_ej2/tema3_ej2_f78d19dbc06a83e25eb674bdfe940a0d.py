import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            new_z = self.z + other.z
            return Vector(new_x, new_y, new_z)
        else:
            raise TypeError("Unsupported operand type. The operand must be a Vector.")
        
def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1 + vector2
    else:
        raise TypeError("Unsupported operand type. The operands must be Vectors.")

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1.norma())  # Imprime la norma del vector v1

v3 = suma_vectores(v1, v2)
print(v3.x, v3.y, v3.z)  # Imprime las coordenadas del vector resultante de la suma

v4 = v1 + v2
print(v4.x, v4.y, v4.z)  # Imprime las coordenadas del vector resultante de la suma usando el operador +
           