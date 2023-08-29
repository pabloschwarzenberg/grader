class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            new_z = self.z + other.z
            return Vector(new_x, new_y, new_z)
        else:
            raise TypeError("Unsupported operand type.")

def suma_vectores(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return v1 + v2
    else:
        raise TypeError("Unsupported operand type.")

# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Calcular la norma del vector v1
print("Norma del vector v1:", v1.norma())

# Sumar dos vectores
v3 = suma_vectores(v1, v2)
print("Suma de vectores:", v3.x, v3.y, v3.z)

# Utilizar la sobrecarga del operador +
v4 = v1 + v2
print("Suma de vectores (operador +):", v4.x, v4.y, v4.z)