class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.num
        r.den=self.den*other.den
        return r

    def __add__(self, other):
        s = Fraccion(0,0)
        if self.den == other.den:
            s.num = self.num + other.num
            s.den = self.num
        elif self.den != other.den:
            s.num = (self.num*other.den) + (other.num*self.den)
            s.den = self.den*other.den
        return s

    def __sub__(self, other):
        resta = Fraccion(0,0)
        if self.den == other.den:
            resta.num = self.num - other.num
            resta.den = self.num
        elif self.den != other.den:
            resta.num = (self.num * other.den) - (other.num * self.den)
            resta.den = self.den * other.den
        return resta

    def __truediv__(self, other):
        division = Fraccion(0,0)
        division.num = self.num*other.den
        division.den = self.den*other.num
        return division

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

if __name__ == "__main__":
    f=input("Ingresa la primera fraccion [a/b]: ")
    f=f.split("/")
    f1=Fraccion(int(f[0]),int(f[1]))
    f=input("Ingresa la segunda fraccion [c/d]: ")
    f=f.split("/")
    f2=Fraccion(int(f[0]),int(f[1]))
    print("La suma es ",f1+f2)
    print("La resta es ",f1-f2)
    print("La multiplicación es ",f1*f2)
    print("La división es ",f1/f2)
         