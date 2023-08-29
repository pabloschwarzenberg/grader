class Fraccion:
    def __init__(self,numerador,denominador):
        self.num=numerador
        self.den=denominador

    def __mul__(self,other):
        r=Fraccion(0,0)
        r.num=self.num*other.num
        r.den=self.den*other.den
        return r

    def __add__(self,other):
        if self.den == other.den:
            suma = Fraccion(self.num + other.num,self.den)
        else:
            nuevo_den = self.den * other.den
            nuevo_num1 = self.num * other.den
            nuevo_num2 = other.num * self.den
            suma = Fraccion(nuevo_num1 + nuevo_num2,nuevo_den)
        return suma
    
    def __sub__(self,other):
        if self.den == other.den:
            resta = Fraccion(self.num - other.num,self.den)
        else:
            nuevo_den = self.den * other.den
            nuevo_num1 = self.num * other.den
            nuevo_num2 = other.num * self.den
            resta = Fraccion(nuevo_num1 - nuevo_num2,nuevo_den)
        return resta

    def __truediv__(self,other):
        nuevo_num = other.den
        nuevo_den = other.num
        division = Fraccion(nuevo_num * self.num,nuevo_den * self.den)
        return division
    
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
