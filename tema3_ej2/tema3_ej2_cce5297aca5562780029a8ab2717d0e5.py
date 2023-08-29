class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def norma(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    
    def __add__(self, otro_vector):
        x_suma = self.x + otro_vector.x
        y_suma = self.y + otro_vector.y
        z_suma = self.z + otro_vector.z
        return Vector(x_suma, y_suma, z_suma)


def suma_vectores(vector1, vector2):
    x_suma = vector1.x + vector2.x
    y_suma = vector1.y + vector2.y
    z_suma = vector1.z + vector2.z
    return Vector(x_suma, y_suma, z_suma)
