class Fraccion:
    def __init__(self,hola,chao):
        self.num=hola
        self.den=chao

    def __mul__(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.num
        r.den=self.den*other.den
        return r
    def __add__(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.den+other.num*self.den
        r.den=self.den*other.den
        return r
    def __sub__(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.den-other.num*self.den
        r.den=self.den*other.den
        return r
    def __truediv__(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.den
        r.den=self.den*other.num
        return r

