# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def norma(self):
        h = (self.x)**2 + (self.y)**2 + (self.z)**2
        h = h**0.5
        return h

def suma_vectores(v1,v2):
    v3_x = v1.x + v2.x
    v3_y = v1.y + v2.y
    v3_z = v1.z + v2.z
    v3 = Vector(v3_x,v3_y,v3_z)
    return v3