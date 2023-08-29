# crea la clase Vector y completa el código de la función suma_vectores usándola
def suma_vectores(v1,v2):
        x=v1.x+v2.x
        y=v1.y+v2.y
        z=v1.z+v2.z
        return Vector(x,y,z)
    
class Vector:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        norma=(self.x**2+self.y**2+self.z**2)**(1/2)
        return norma

    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.z+other.z
        return Vector(x,y,z)


if __name__=="__main__":
    a=Vector(1,2,3)
    b=Vector(3,4,5)
    c=suma_vectores(a,b)
    c=a+b