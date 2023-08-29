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
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            return Vector(x, y, z)
        else:
            raise TypeError("El objeto pasado no es un Vector")

def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1 + vector2
    else:
        raise TypeError("Los objetos pasados no son de tipo Vector")

# Ejemplo de uso
vector1 = Vector(1, 2, 3)
vector2 = Vector(4, 5, 6)

# Calculando la norma del vector1
print(vector1.norma())  # Resultado: 3.7416573867739413

# Sumando dos vectores
resultado = suma_vectores(vector1, vector2)
print(resultado.x, resultado.y, resultado.z)  # Resultado: 5 7 9

# Utilizando la sobrecarga del operador '+'
resultado = vector1 + vector2
print(resultado.x, resultado.y, resultado.z)  # Resultado: 5 7 9
