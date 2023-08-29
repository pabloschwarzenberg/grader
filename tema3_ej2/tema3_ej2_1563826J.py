# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    import math    
    def norma(self):
        norma=(self.x**2+self.y**2+self.z**2)**(1/2)
        return norma 
    def __add__(v1,v2):
        a=v1.x+v2.x
        b=v1.y+v2.y
        c=v1.z+v2.z
        d=Vector(a,b,c)
        return d
v1=Vector(1,2,3)
v2=Vector(2,3,4)

def suma_vectores(v1,v2):
    a=v1.x+v2.x
    b=v1.y+v2.y
    c=v1.z+v2.z
    d=Vector(a,b,c)
    return d

print(suma_vectores(v1,v2).x)
print(suma_vectores(v1,v2).y)
print(v1.norma())