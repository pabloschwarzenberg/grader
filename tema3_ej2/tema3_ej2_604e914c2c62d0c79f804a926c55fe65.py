# crea la clase Vector y completa el código de la función suma_vectores usándola
class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        return ((self.x**2+self.y**2+self.z**2)**(1/2))
    def __add__(a,b):
        p=a.x+b.x
        q=a.y+b.y
        r=a.z+b.z
        return vector(p,q,r)
    def __str__(self):
        u=str(self.x)+","+str(self.y)+","+str(self.z)
        return u

def suma_vectores():
    v1=vector(1,2,3)
    v2=vector(3,4,5)
    v3=v1+v2
    return vector.__add__(v1,v2)           