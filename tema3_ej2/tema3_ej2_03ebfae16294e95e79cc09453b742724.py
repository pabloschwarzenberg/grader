# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Unsupported operand type for +")

def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1 + vector2
    else:
        raise TypeError("Unsupported operand types for vector addition")

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1.norma())  # Imprime: 3.7416573867739413
print(v2.norma())  # Imprime: 8.774964387392123

v3 = suma_vectores(v1, v2)
print(v3.x, v3.y, v3.z)  # Imprime: 5 7 9

v4 = v1 + v2
print(v4.x, v4.y, v4.z)  # Imprime: 5 7 9