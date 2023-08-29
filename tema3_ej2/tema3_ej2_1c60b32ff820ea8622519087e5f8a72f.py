class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def suma_vectores(v1,v2):
        return Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)
    
    def norma(v1):
        v1 = (v1.x + v1.y + v1.z)
        v1 = v1**(1/2)
        return v1
           