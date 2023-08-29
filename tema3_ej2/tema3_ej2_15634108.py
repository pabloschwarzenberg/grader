import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,other):
        x_nuevo=self.x+other.x
        y_nuevo=self.y+other.y
        z_nuevo=self.z+other.z
        return Vector(x_nuevo,y_nuevo,z_nuevo)
    def norma(self):
        norma=math.sqrt(((self.x)**2)+((self.y)**2)+((self.z)**2))
        return norma
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"
def suma_vectores(v1,v2):
    x=v1.x+v2.x
    y=v1.y+v2.y
    z=v1.z+v2.z
    return Vector(x,y,z)