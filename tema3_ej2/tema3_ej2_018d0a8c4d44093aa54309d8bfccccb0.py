# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def norma(self):
        norm= (self.x)**2+(self.y)**2+(self.z)**2
        nor = norm**(1/2)
        return nor
    def __add__(self,other):
        xa= self.x + other.x
        ya = self.y + other.y
        za = self.z + other.z
        vf= Vector(xa,ya,za)
        return vf
def suma_vectores(v1,v2):
    return v1+v2          