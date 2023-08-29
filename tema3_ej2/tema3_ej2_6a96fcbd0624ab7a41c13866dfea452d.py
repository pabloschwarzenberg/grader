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
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise ValueError("La operación de suma solo es válida entre objetos de la clase Vector")

def suma_vectores(a, b):
    if isinstance(a, Vector) and isinstance(b, Vector):
        return a + b
    else:
        raise ValueError("La función suma_vectores solo acepta objetos de la clase Vector como parámetros")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear objetos de la clase Vector
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    
    # Calcular la norma del vector v1
    print("Norma de v1:", v1.norma())
    
    # Sumar dos vectores
    v3 = suma_vectores(v1, v2)
    print("Suma de v1 y v2:", v3.x, v3.y, v3.z)
    
    # Sumar dos vectores utilizando la sobrecarga del operador +
    v4 = v1 + v2
    print("Suma de v1 y v2 (usando sobrecarga de operador):", v4.x, v4.y, v4.z)
