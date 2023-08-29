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
            raise TypeError("Operación no válida. Se requiere un objeto de la clase Vector.")

def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        x_sum = vector1.x + vector2.x
        y_sum = vector1.y + vector2.y
        z_sum = vector1.z + vector2.z
        return Vector(x_sum, y_sum, z_sum)
    else:
        raise TypeError("Operación no válida. Se requieren objetos de la clase Vector.")

# Ejemplo de uso
vector1 = Vector(1, 2, 3)
vector2 = Vector(4, 5, 6)

# Cálculo de la norma del vector1
norma_vector1 = vector1.norma()
print("Norma del vector1:", norma_vector1)

# Suma de los vectores vector1 y vector2 usando el método __add__
vector_suma = vector1 + vector2
print("Suma de los vectores (usando el método __add__):", vector_suma.x, vector_suma.y, vector_suma.z)

# Suma de los vectores vector1 y vector2 usando la función suma_vectores
vector_suma_funcion = suma_vectores(vector1, vector2)
print("Suma de los vectores (usando la función suma_vectores):", vector_suma_funcion.x, vector_suma_funcion.y, vector_suma_funcion.z)

