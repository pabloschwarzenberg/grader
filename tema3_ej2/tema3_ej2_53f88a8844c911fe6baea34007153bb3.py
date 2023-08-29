# completa el código de la función
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def norma(self):
        self.norma=(self.x**2+self.y**2+self.z**2)**(1/2)
        return self.norma
        
    def __add__(self,other):
        rx=self.x+other.x
        ry=self.y+other.y
        rz=self.z+other.z
        return Vector(rx,ry,rz)

def suma_vectores(a,b):
    r=a+b
    return r