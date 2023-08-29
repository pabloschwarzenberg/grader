class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,other): 
        a=Fraccion(0,0)
        a.num=self.num*other.num
        a.den=self.den*other.den
        return a

    def __div__(self,other):
        b=Fraccion(0,0)
        b.num=self.num*other.den
        b.den=self.den*other.num
        return b

    def __add__(self,other):
        c=Fraccion(0,0)
        c.den=self.den*other.den
        c.num=(self.num*other.den)+(other.num*self.den)
        return c

    def __sub__(self,other):
        d=Fraccion(0,0)
        d.den=self.den*other.den
        d.num=(self.num*other.den)-(other.num*self.den)
        return d

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
    d=f1.__div__(f2)
    m=f1.__mul__(f2)
    a=f1.__add__(f2)
    s=f1.__sub__(f2)
    print("La suma es ",a.__repr__())
    print("La resta es ",s.__repr__())
    print("La multiplicación es ",m.__repr__())
    print("La división es ",d.__repr__())
         