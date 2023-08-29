from math import sqrt

class Vector:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def norma(self):
        norma=sqrt((self.x*self.x)+(self.y*self.y)+(self.z*self.z))
        return(norma)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y,self.z+other.z)

    def suma_vectores(self,other):
        vx=self.x+other.x
        vy=self.y+other.y
        vz=self.z+other.z
        return(vx,vy,vz)

    def __str__(self):
        return ("("+str(self.x)+","+str(self.y)+","+str(self.z)+")")