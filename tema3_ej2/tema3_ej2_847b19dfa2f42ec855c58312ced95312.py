# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
       self.x=x
       self.y=y
       self.z=z
    def norma(self):
        norma=round(((self.x**2+ self.y**2 +self.z**2)**1/2),0)
        return norma
    def __add__(self,v2):
        return suma_vectores(self, v2)


def suma_vectores(v1,v2):
    x=(v1.x +v2.x)
    y=(v1.y +v2.y)
    z=(v1.z +v2.z)
    v3= Vector(x,y,z)
    return v3

        
               