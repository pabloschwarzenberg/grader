class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador
        self.a_numero = []

    def __mul__(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.num
        r.den=self.den*other.den
        return r

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return "{0}/{1}".format(num,den)
    
    def __add__(self,other):
        if self.den == other.den:
          suma = self.num + other.num
          return "{0}/{1}".format(suma,self.den)
        else:
          num = self.num*other.den + other.num*self.den
          den = self.den * other.den
          return "{0}/{1}".format(num,den)
          
    def __sub__(self,other):
        if self.den == other.den:
          suma = self.num - other.num
          return "{0}/{1}".format(suma,self.den)
        else:
          num = self.num*other.den - other.num*self.den
          den = self.den * other.den
          return "{0}/{1}".format(num,den)
          
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
            
    def __str__(self):
        print("La suma es ",self.__sum__())
        print("La resta es ",self.__sub__())
        print("La multiplicación es ",self.__mul__())
        print("La división es ",self.__truediv__())
            

       
    

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
         