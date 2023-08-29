class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            new_z = self.z + other.z
            return Vector(new_x, new_y, new_z)
        else:
            raise TypeError("La operación + solo es válida entre objetos de la clase Vector")

def suma_vectores(v1, v2):
    return v1 + v2

