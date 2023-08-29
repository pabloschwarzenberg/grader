class Vector:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
        
    def norma(self):
        n=(self.x**2+self.y**2+self.z**2)**0.5
        return n
        
    def __add__(self,other):
        new=Vector()
        new.x=self.x+other.x
        new.y=self.y+other.y
        new.z=self.z+other.z
        return new
        
    def __str__(self):
        return str(self.x)+","+str(self.y)+","+str(self.z)

def suma_vectores(v1,v2):
    new=Vector()
    new.x=v1.x+v2.x
    new.y=v1.y+v2.y
    new.z=v1.z+v2.z
    return new

if __name__=="__main__":
    print("Primer vector")
    x1=int(input("Ingrese coordenada x: "))
    y1=int(input("Ingrese coordenada y: "))
    z1=int(input("Ingrese coordenada z: "))
    primer=Vector(x1,y1,z1)
    print("Segundo vector")
    x2=int(input("Ingrese coordenada x: "))
    y2=int(input("Ingrese coordenada y: "))
    z2=int(input("Ingrese coordenada z: "))
    segundo=Vector(x2,y2,z2)
    operacion=primer+segundo
    print(operacion)
    