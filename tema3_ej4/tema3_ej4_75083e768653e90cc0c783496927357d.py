class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,other):
        res=Fraccion(0,0)
        res.num=self.num*other.num
        res.den=self.den*other.den
        return res

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

    def __add__(self, other):
        sol=Fraccion(0,0)
        sol.num=(self.num*other.den)+(other.num*self.den)
        sol.den=self.den*other.den
        return sol
    def __sub__(self, other):
        sol=Fraccion(0,0)
        sol.num=(self.num*other.den)-(other.num*self.den)
        sol.den=self.den*other.den
        return sol
    def __truediv__(self, other):
        sol=Fraccion(0,0)
        sol.num=self.num*other.den
        sol.den=self.den*other.num
        return sol
if __name__ == "__main__":
    i=input("Ingresa la primera fraccion [a/b]: ")
    i=i.split("/")
    i1=Fraccion(int(i[0]),int(i[1]))
    i=input("Ingresa la segunda fraccion [c/d]: ")
    i=i.split("/")
    i2=Fraccion(int(i[0]),int(i[1]))
    print("La suma es ",i1+i2)
    print("La resta es ",i1-i2)
    print("La multiplicación es ",i1*i2)
    print("La división es ",i1/i2)
