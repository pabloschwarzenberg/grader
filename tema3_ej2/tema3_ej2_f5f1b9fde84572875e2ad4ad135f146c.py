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
            raise TypeError("La operación de suma solo es válida para objetos de la clase Vector")

    def __repr__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)



def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1 + vector2
    else:
        raise TypeError("La función suma_vectores solo acepta objetos de la clase Vector como argumentos")


# Ejemplo de uso
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Vector 1:", v1)
print("Vector 2:", v2)

norma_v1 = v1.norma()
print("Norma de Vector 1:", norma_v1)

suma = suma_vectores(v1, v2)
print("Suma de Vector 1 y Vector 2:", suma)
