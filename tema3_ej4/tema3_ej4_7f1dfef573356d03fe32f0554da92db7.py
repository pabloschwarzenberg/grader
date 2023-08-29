def divisores(a):
    m = []
    divisor = 1
    while divisor < a :
        if a % divisor == 0 :
            m.append(divisor)
        divisor += 1
    m.remove(1)
    return m

def reducir(a,b):
    m = divisores(a)
    n = divisores(b)
    g = []
    for i in range(len(m)):
        for j in range(len(n)):
            if m[i] == n[j]:
                a = int(a/m[i])
                b = int(b/m[i])
                break
        m = divisores(a)
        n = divisores(b)
    g.append(a)
    g.append(b)
    return g

class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,other):
        a= self.num * other.num
        b= self.den * other.den
        return Fraccion(a,b)
    def __add__(self,other):
        a = (self.num * other.den) + (other.num * self.den)
        b = self.den * other.den
        return Fraccion(reducir(a,b)[0],reducir(a,b)[1])
    def __sub__(self,other):
        a = (self.num * other.den) - (other.num * self.den)
        b = self.den * other.den
        return Fraccion(reducir(a,b)[0],reducir(a,b)[1])
    def __truediv__(self,other):
        a= self.num * other.den
        b= self.den * other.num
        return Fraccion(a,b)
        
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