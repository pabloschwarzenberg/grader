import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.vector=(self.x,self.y,self.z)
    def norma(self):
        norma=math.sqrt((float(self.x)*float(self.x)+float(self.y)*float(self.y)+float(self.z)*float(self.z)))
        return norma
    def __add__(self, v):
        r=Vector(0,0,0)
        r.x = self.x+v.x
        r.y = self.y + v.y
        r.z = self.z + v.z
        self.vector=(self.x,self.y,self.z)
        return r
def suma_vectores(v1,v2):
    sumadv = [(int(v1.x)+int(v2.x)),(int(v1.y)+int(v2.y)),(int(v1.z)+int(v2.z))]
    return Vector(sumadv[0],sumadv[1],sumadv[2])