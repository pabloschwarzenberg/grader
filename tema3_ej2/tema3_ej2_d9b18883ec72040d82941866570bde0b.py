class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def norma(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    
    def __add__(self, otro_vector):
        suma_x = self.x + otro_vector.x
        suma_y = self.y + otro_vector.y
        suma_z = self.z + otro_vector.z
        return Vector(suma_x, suma_y, suma_z)


def suma_vectores(v1, v2):
    return v1 + v2
