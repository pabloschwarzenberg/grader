
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,other):  
        r=Vector(0,0,0)
        r.x=(self.x+other.x)
        r.y=(self.y+other.y)
        r.z=(self.z+other.z)
        return r
    
    def norma(self):
        norma=((self.x)**2 + (self.y)**2 + (self.z)**2)**(1/2)
        return norma

def suma_vectores(v1,v2):
    return v1+v2          