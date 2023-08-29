# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        return ((self.x**2)+(self.y**2)+(self.z**2))**(1/2)
    def __add__(self, other):
        return Vector((other.x+self.x),(other.y+self.y),(other.z+self.z))
def suma_vectores(x,y):
    return Vector((x.x + y.x), (x.y + y.y), (x.z + y.z))