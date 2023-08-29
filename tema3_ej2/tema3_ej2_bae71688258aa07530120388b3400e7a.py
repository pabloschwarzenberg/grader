import math
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def norma(self):
        a = self.x
        b = self.y
        c = self.z
        if a == b == c:
            return(1)
        else:
            k = math.sqrt(a+b+c)
            return(k)
    def suma_vectores(v1,v2):
        a = v1 + v2
        return(a)          