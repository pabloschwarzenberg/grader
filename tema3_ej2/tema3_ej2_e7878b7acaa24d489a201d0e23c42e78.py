class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        return [self.x,self.y,self.z]
    
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.z+other.z
        
        return Vector(x,y,z)

    def norma(self):
        a=self.x**2
        b=self.y**2
        c=self.z**2
        d=(a+b+c)**(int(1/2))
        return d
        
def suma_vectores(v1,v2):
    v3=v1+v2
    return v3           