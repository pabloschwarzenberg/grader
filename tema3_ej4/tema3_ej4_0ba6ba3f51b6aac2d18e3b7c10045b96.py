class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador
    def __add__(self,other):
        s=Fraccion(0,0)
        denomin=self.num*other.num
        num1=self.num*(denomin//self.den)
        num2=other.num*(denomin//other.den)
        s.den=denomin
        s.num=num1+num2
        return s
    def __sub__(self,other):
        k=Fraccion(0,0)
        denomin=self.num*other.num
        num1=self.num*(denomin//self.den)
        num2=other.num*(denomin//other.den)
        k.num=num1-num2
        k.den=denomin
        return k
    def __mul__(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.num
        r.den=self.den*other.den
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
         