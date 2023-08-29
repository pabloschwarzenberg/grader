class Fraccion:
    def __init__(self,numerador,denominador): 
        self.num=numerador
        self.den=denominador
        # mi amoor, sea x/y una fraccion su numerador es x y su denominador es y.
        
    def __add__(self,other):
        sumax=(((self.den*other.den)/self.den)*self.num)+(((self.den*other.den)/other.den)*other.num)
        print(sumax)
        sumay=self.den*other.den
        print(sumay)
        return Fraccion(sumax,sumay)
    
    
    def __mul__(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.num
        r.den=self.den*other.den
        return r

    def __sub__(self,other):
        subx=(((self.den*other.den)/self.den)*self.num)-(((self.den*other.den)/other.den)*other.num)
        print(subx)
        suby=self.den*other.den
        print(suby)
        return Fraccion(subx,suby)
    
    def __truediv__(self,other):
        divx=self.num*other.den
        divy=self.den*other.num
        return Fraccion(divx,divy)
    
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
         