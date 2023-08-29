# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)



    def __add__(self,vec):
        x=self.x + vec.x
        y=self.y+ vec.y
        z=self.z + vec.z
        return Vector(x,y,z)

    def __repr__(self):
        return "{},{},{}".format(self.x,self.y,self.z)
vec1=Vector(1,2,3)
vec2=Vector(1,2,3)
print(vec1+vec2)
def suma_vectores(a,vec):
        x=a.x + vec.x
        y=a.y+ vec.y
        z=a.z + vec.z
        return Vector(x,y,z)
print(suma_vectores(vec1,vec2))