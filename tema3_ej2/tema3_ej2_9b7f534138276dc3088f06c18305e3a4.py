class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        norma={{self.x}**2+{self.y}**2+{self.z}**2}**{1/2}
        return norma
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.z+other.z
        vector=(x,y,z)
        return vector

def suma_vectores(v1,v2):
    suma=v1+v2
    return suma
