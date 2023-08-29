import math
class Vector:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        lista=[]
        vector=[self.x,self.y,self.z]
        for i in vector:
            a=i*i
            lista.append(a)
        b=0
        c=0
        while c<len(vector):
            b=(b+lista[c])
            c=c+1
        norma=math.sqrt(b)
        return norma

    def __str__(self):
        return "{0} {1} {2}".format(self.x,self.y,self.z)

    def __add__(self,other):
        c=Vector()
        c.x=self.x+other.x
        c.y=self.y+other.y
        c.z=self.z+other.z
        return c

def suma_vectores(v1,v2):
    return v1+v2

if __name__=="__main__":
    a=Vector(1,2,3)
    b=Vector(4,5,6)
    c=a+b
    print(c)
    print(suma_vectores(Vector(1,2,3),Vector(4,5,6)))
    print(a.norma())
           