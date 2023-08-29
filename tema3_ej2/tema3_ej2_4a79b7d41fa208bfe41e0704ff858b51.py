import math

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        norma_calculado = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return norma_calculado

    def __add__(self,other):
        vector_suma = []
        vector_suma.append(self.x+other.x)
        vector_suma.append(self.y+other.y)
        vector_suma.append(self.z+other.z)
        return vector_suma
    
def suma_vectores(v1,v2):
    
        suma = []
        suma.append(v1.x+v1.x)
        suma.append(v1.y+v1.y)
        suma.append(v1.z+v1.z)

        return Vector(suma[0],suma[1],suma[2])