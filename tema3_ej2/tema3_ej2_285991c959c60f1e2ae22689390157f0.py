# crea la clase Vector y completa el código de la función suma_vectores usándola

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
        norma_vector=((self.x)**2+(self.y)**2+(self.z)**2)**(1/2)
        return norma_vector
    
def suma_vectores(v1,v2):
    v1+v2
    return v1+v2



#def suma_vectores(v1,v2):
 # return 
           