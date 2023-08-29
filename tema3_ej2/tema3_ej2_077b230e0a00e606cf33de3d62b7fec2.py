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
            x_sum = self.x + other.x
            y_sum = self.y + other.y
            z_sum = self.z + other.z
            return Vector(x_sum, y_sum, z_sum)
        else:
            raise TypeError("Operandos inválidos para la suma de vectores.")

def suma_vectores(v1, v2):
    return v1 + v2
# Ejemplo de uso
if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    
    print(v1.norma())  # 3.7416573867739413
    print(v2.norma())  # 8.774964387392123
    
    v3 = suma_vectores(v1, v2)
    print(v3.x, v3.y, v3.z)  # 5 7 9
    
    v4 = v1 + v2
    print(v4.x, v4.y, v4.z)  # 5 7 9
