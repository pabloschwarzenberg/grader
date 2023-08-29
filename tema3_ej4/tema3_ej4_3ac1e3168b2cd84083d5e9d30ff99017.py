class Fraccion:
    def __init__(self,numerador,denominador):
    def truediv(self,other):
        r=Fraccion(0,0)
        r.num=self.num/(1/other.den)
        r.den=self.den/(1/other.num)
        return r

    def add(self,other):
        m=Fraccion(0,0)
        m.num=(self.numother.den)+(self.denother.num)
        m.den=self.denother.den
        return m 

    def sub(self,other):
        m=Fraccion(0,0)
        m.num=(self.numother.den)-(self.denother.num)
        m.den=self.denother.den
        return m

    def mul(self,other):
        r=Fraccion(0,0)
        r.num=self.numother.num
        r.den=self.denother.den
        return r

    def repr(self):
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
         