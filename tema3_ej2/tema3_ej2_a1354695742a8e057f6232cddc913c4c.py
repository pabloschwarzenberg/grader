class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        norma=((self.x**2)+(self.y**2)+(self.z**2))**(1/2)
        return norma
    def __add__(self,other):
        v=Vector(0,0,0)
        v.x=(self.x+other.x)
        v.z = (self.z + other.z)
        v.y = (self.y + other.y)
        return v
def suma_vectores(v1,v2):
    vs=v1+v2
    return vs

           