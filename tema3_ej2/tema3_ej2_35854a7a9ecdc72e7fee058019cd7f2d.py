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
            raise TypeError("Operación no válida. Se requiere un objeto de la clase Vector")

def suma_vectores(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return v1 + v2
    else:
        raise TypeError("Se requieren objetos de la clase Vector como parámetros")

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = suma_vectores(v1, v2)

print(v1.norma())  # 3.7416573867739413
print(v2.norma())  # 8.774964387392123
print(v3.norma())  # 9.539392014169456