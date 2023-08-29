# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            return Vector(x, y, z)
        else:
            raise TypeError("Operands must be of type Vector")

def suma_vectores(v1, v2):
    return v1 + v2

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

v3 = suma_vectores(v1, v2)
print(v3.x, v3.y, v3.z)  # Imprime: 5 7 9

norma_v3 = v3.norma()
print(norma_v3)  # Imprime: 12.84523257866513

           