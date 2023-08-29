# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:

    def __init__(self,x,y,z):

        self.x = x
        self.y = y
        self.z = z

    def norma(self):

        n = (self.x)**2 + (self.y)**2 + (self.z)**2
        k = n**0.5
        return k

    def __add__(self,other):
    
        x = self.x+other.x
        y = self.y+other.y
        z = self.z+other.z
        
        return Vector(x,y,z)


def suma_vectores(self,other):
    
        v = self+other
        
        return v
           