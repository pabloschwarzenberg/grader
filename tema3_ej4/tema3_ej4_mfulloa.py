class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,other):
        if isinstance(other,Fraccion):
            r.num=self.num*other.num
            r.den=self.den*other.den
        elif isinstance(other,int) or isinstance(other,float):
            r.num=self.num*other
            r.den=self.den        
        r=Fraccion(r.num,r.den)
        return r
    def __add__(self,other):
        if isinstance(other,Fraccion):
            a.num=self.num*other.den+self.den*other.num
            a.den=self.den*other.den
        elif isinstance(other,int) or isinstance(other,float):
            a.num=self.num+other*self.den
            a.den=self.den
        a=Fraccion(a.num,a.den)
        return a
    def __sub__(self,other):
        if isinstance(other,Fraccion):
            m.num=self.num*other.den-self.den*other.num
            m.den=self.den*other.den
        elif isinstance(other,int) or isinstance(other,float):
            m.num=self.num-other*self.den
            m.den=self.den
        m=Fraccion(m.num,m.den)
        return m

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
         

