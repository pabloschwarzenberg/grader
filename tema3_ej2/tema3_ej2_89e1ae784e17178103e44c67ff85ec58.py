# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        return ((self.x)**2 + (self.y)**2 + (self.z)**2)**(1/2)
    def __repr__(self):
        return str(self.x)+","+str(self.y)+","+str(self.z)
    def __add__(self, other):
        v3=Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        return v3


def suma_vectores(v1,v2):
    return v1.__add__(v2)
v1=Vector(0.5773502691896258,0.5773502691896258,0.5773502691896258)
v2=Vector(1,2,3)
v3=suma_vectores(v1,v2)
print(v3)