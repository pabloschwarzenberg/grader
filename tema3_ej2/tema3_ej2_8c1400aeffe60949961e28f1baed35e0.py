class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        norma=((self.x)**2+(self.y)**2+(self.z)**2)**(1/2)
        return norma

    def __add__(self,other):
        vx=self.x+other.x
        vy=self.y+other.y
        vz=self.z+other.z
        vs=Vector(vx,vy,vz)
        return vs

def suma_vectores(v1,v2):
    return v1+v2

        
        
        
        
        
        
 