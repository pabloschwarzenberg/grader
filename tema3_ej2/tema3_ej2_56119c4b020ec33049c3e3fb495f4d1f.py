# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        if isinstance(other, Vector3D):
            x_sum = self.x + other.x
            y_sum = self.y + other.y
            z_sum = self.z + other.z
            return Vector3D(x_sum, y_sum, z_sum)
        else:
            raise TypeError("Operación no válida. Se requiere un objeto de la clase Vector3D.")

def suma_vectores(v1, v2):
    if isinstance(v1, Vector3D) and isinstance(v2, Vector3D):
        x_sum = v1.x + v2.x
        y_sum = v1.y + v2.y
        z_sum = v1.z + v2.z
        return Vector3D(x_sum, y_sum, z_sum)
    else:
        raise TypeError("Operación no válida. Se requieren objetos de la clase Vector3D.")

           