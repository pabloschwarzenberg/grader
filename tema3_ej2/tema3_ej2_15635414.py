# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector :
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def norma(self):
        normav = math.sqrt ((self.x)**2 + (self.y)**2 + (self.z)**2)
        return normav
    
    def __add__(self, v):
        sumax=self.x+v.x
        sumay=self.y+v.y
        sumaz=self.z+v.z
        sumavectores=Vector(sumax,sumay,sumaz)
        return sumavectores
    def __str__(self):
        coor="Las coordenadas son: "+str(self.x)+", "+str(self.y)+", "+str(self.z)+"."
        return  coor
def suma_vectores(v1,v2):
    resultado=Vector((v1.x+v2.x), (v1.y+v2.y), (v1.z+v2.z))
    return resultado    


           