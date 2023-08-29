# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector():
    x = 0
    y = 0
    z = 0
    def __init__(self, x, y, z):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)
    def norma(self):
        return (self.x**2 + self.y**2 + self.z**2)**(1/2)

def suma_vectores(v1, v2):
    x=(v1.x+v2.x)
    y=(v1.y+v2.y)
    z=(v1.z+v2.z)
    v3=Vector(x, y, z)
    return v3
        