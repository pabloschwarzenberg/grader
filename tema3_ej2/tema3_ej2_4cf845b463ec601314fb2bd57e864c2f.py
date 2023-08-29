# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"
        

    def norma(self):
        return(self.x*2 + self.y*2+ self.z*2)#*(1/2)
        #return round(n,2)

    def __add__(self,other):
        return Vector(self.x + other.x,self.y + other.y,self.z + other.z) #,self.z + other.z
    
def suma_vectores(v1,v2):
        vs = Vector(0,0,0)
        vs = v1 + v2
        return vs
           