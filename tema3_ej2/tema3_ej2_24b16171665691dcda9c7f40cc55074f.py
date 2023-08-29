# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z    
    def norma(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1/2)    
    def __add__(self, otro_vector):
        vectorx = self.x + otro_vector.x
        vectory = self.y + otro_vector.y
        vectorz= self.z + otro_vector.z
        return Vector(vectorx, vectory, vectorz)
def suma_vectores(a, b):
    return a + b


    
