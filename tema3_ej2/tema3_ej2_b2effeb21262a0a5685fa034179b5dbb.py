# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def suma_vectores(self,v1,v2):
        suma =Vector(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z)
        return suma
    def norma(self):
        raiz=(self.x**2+self.y**2+self.z**2)**0.5
        return True
        