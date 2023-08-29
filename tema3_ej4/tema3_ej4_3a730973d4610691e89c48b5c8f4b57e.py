class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador
    
    def __add__(self,other):
        if self.den==other.den:
            sum1=self.num+other.num
            sum2=self.den
            return Fraccion(sum1,sum2)
        if self.den!=other.den:
            sum3=self.num*other.den
            sum4=self.den*other.den
            sum5=other.num*self.den
            sum6=other.den*self.den
            sum7=sum3+sum5
            return Fraccion(sum7,sum6)
    
    def __sub__(self,other):
        if self.den==other.den:
            res1=self.num-other.num
            res2=self.den
            return Fraccion(sum1,sum2)
        if self.den!=other.den:
            res3=self.num*other.den
            res4=self.den*other.den
            res5=other.num*self.den
            res6=other.den*self.den
            res7=res3-res5
            return Fraccion(res7,res6)
     
    def __truediv__(self,other):
        div1=self.num*other.den
        div2=self.den*other.num
        fracciondiv = Fraccion(div1,div2)
        return fracciondiv
    
    def __mul__(self,other):
        mul1=self.num*other.num
        mul2=self.den*other.den
        fraccionmul = Fraccion(mul1,mul2)
        return fraccionmul

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
         