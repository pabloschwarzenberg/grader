class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def norma(self):
        norma= ((self.x)**2 + (self.y)**2 + (self.z)**2)**(1/2)
        print("La norma entre los vectores es:", norma)
def suma(a,b):
        return Vector(a.x+b.x, a.y+b.y, a.z+b.z)
if __name__ == "__main__":
    print("Ingrese los puntos (x,y,z) de su vector:")
    x= int(input("Ingrese valor de x:"))
    y= int(input("Ingrese valor de y:"))
    z= int(input("Ingrese valor de z:"))
    a=Vector(x,y,z)
    b=Vector(1,2,3) 
    c=suma(a,b)
    a.norma()
    




           