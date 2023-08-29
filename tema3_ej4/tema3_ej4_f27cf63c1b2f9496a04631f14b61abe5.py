class Fraccion:
    def _init_(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def _mul_(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.num
        r.den=self.den*other.den
        return r
        
    def _truediv_(self,other):
        r=Fraccion(0,0)
        r.num=self.num/(1/other.den)
        r.den=self.den/(1/other.num)
        return r
        
    def _add_(self,other):
        m=Fraccion(0,0)
        m.num=(self.num*other.den)+(self.den*other.num)
        m.den=self.den*other.den
        return m      

    def _sub_(self,other):
        m=Fraccion(0,0)
        m.num=(self.num*other.den)-(self.den*other.num)
        m.den=self.den*other.den
        return m
    def _repr_(self):
        entero=self.num//self.den
        if entero>0:
            resto=self.num%self.den
            if resto>0:
                return "{0} {1}/{2}".format(entero,resto,self.den)
            else:
                return "{0}".f

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
         