class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def norma(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def __add__(self, other):
        if isinstance(other, Vector):
            sum_x = self.x + other.x
            sum_y = self.y + other.y
            sum_z = self.z + other.z
            return Vector(sum_x, sum_y, sum_z)
        else:
            raise TypeError("Operands must be of type Vector")

def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        sum_x = vector1.x + vector2.x
        sum_y = vector1.y + vector2.y
        sum_z = vector1.z + vector2.z
        return Vector(sum_x, sum_y, sum_z)
    else:
        raise TypeError("Operands must be of type Vector")


# Ejemplo de uso
vector1 = Vector(1, 2, 3)
vector2 = Vector(4, 5, 6)

# Calculando la norma del vector1
norma_vector1 = vector1.norma()
print("Norma del vector1:", norma_vector1)

# Sumando dos vectores utilizando el método __add__
vector3 = vector1 + vector2
print("Suma de vector1 y vector2:", vector3.x, vector3.y, vector3.z)

# Sumando dos vectores utilizando la función suma_vectores
vector4 = suma_vectores(vector1, vector2)
print("Suma de vector1 y vector2:", vector4.x, vector4.y, vector4.z)
