# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def norma(self):
        self.norma=((self.x**2) + (self.y**2) + (self.z**2))**(1/2)
        return self.norma
        
    def __add__(self,v2):
        x = self.x + v2.x
        y = self.y + v2.y
        z = self.z + v2.z
        vectorsuma=Vector(x,y,z)
        return vectorsuma
    

def suma_vectores(v1,v2):
    x = v1.x + v2.x
    y = v1.y + v2.y
    z = v1.z + v2.z
    vectorsuma=Vector(x,y,z)
    return vectorsuma
           