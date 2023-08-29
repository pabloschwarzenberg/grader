class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        norma=((self.x**2)+(self.y**2)+(self.z**2))**(1/2)
        return norma
    def __add__(self,other):
        v=Vector(0,0,0)
        v.x=(self.x+other.x)
        v.z = (self.z + other.z)
        v.y = (self.y + other.y)
        return v
def suma_vectores(v1,v2):
    vs=v1+v2
    return vs

class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,other):
        r = Fraccion(0, 0)
        r.num = self.num * other.num
        r.den = self.den * other.den
        return r
    def __truediv__(self,other):
        r = Fraccion(0, 0)
        r.num = self.num * other.den
        r.den = self.den * other.num
        return r
    def __add__(self, other):
        r = Fraccion(0, 0)
        r.num = (self.num*other.den) + (other.num*self.den)
        r.den = self.den*other.den
        return r
    def __sub__(self, other):
        r = Fraccion(0, 0)
        r.num = (self.num * other.den) - (other.num * self.den)
        r.den = self.den * other.den
        return r


    def __repr__(self):
        entero=self.num//self.den
        if entero>0:
            resto=self.num%self.den
            if resto>0:
                return "{0} {1}/{2}".format(entero,resto,self.den)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.num,self.den)
        
    


    def a_numero(self):
        return self.num/self.den
print(1/2 + 3/4)
print(1/2 - 3/4)
