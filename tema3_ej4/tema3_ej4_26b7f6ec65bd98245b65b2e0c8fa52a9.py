class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,other):
        rnum=self.num*other.num
        rden=self.den*other.den
        r=Fraccion(rnum,rden)
        return r
        
    def __add__(self,other):
        rnum=(self.num*other.den)+(self.den*other.num)
        rden=(self.den*other.den)
        r=Fraccion(rnum,rden)
        return r

    def a_numero(self):
        return self.num/self.den
