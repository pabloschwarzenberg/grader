class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

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
    def suma(self,a):
       r=((self.num*a.den+a.num*self.den)/(a.den*self.den))
       return (r)

    def resta(self,a):
       r=((self.num*a.den-a.num*self.den)/(a.den*self.den))
       return r
    def division(self,a):
        m=(self.num*a.den)/(self.den*a.num)
        return m

if __name__ == "__main__":
    a=int(input("Ingresa el numerados de la primera faccion: "))
    b=int(input("Ingresa el denominador de la primera faccion: "))
    f1=(Fraccion(a,b))
    c=int(input("Ingresa el numerador de la segunda faccion: "))
    d=int(input("Ingresa el denominador de la segunda faccion: "))
    f2=(Fraccion(c,d))
    print("La suma es ",Fraccion.suma(f1,f2))
    print("La resta es ",Fraccion.resta(f1,f2))
    print("La multiplicación es ",f1*f2)
    print("La división es ",Fraccion.division(f1,f2))
         