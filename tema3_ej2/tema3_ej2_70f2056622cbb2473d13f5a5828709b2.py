class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def norma(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    
    def __add__(self, otro_vector):
        if isinstance(otro_vector, Vector):
            suma_x = self.x + otro_vector.x
            suma_y = self.y + otro_vector.y
            suma_z = self.z + otro_vector.z
            return Vector(suma_x, suma_y, suma_z)
        else:
            raise TypeError("El objeto a sumar no es un vector")

def suma_vectores(vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        suma_x = vector1.x + vector2.x
        suma_y = vector1.y + vector2.y
        suma_z = vector1.z + vector2.z
        return Vector(suma_x, suma_y, suma_z)
    else:
        raise TypeError("Los objetos a sumar no son vectores")