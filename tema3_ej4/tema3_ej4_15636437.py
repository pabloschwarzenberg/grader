class Fraccion:
    def __init__(self,a=0,b=1):
        self.a=a
        self.b=b

    def __mul__(self,other):
        new=Fraccion()
        new.a=self.a*other.a
        new.b=self.b*other.b
        return new

    def __add__(self,other):
        new=Fraccion()
        new.a=self.a*other.b+other.a*self.b
        new.b=self.b*other.b
        return new

    def __sub__(self,other):
        new=Fraccion()
        new.a=self.a*other.b-other.a*self.b
        new.b=self.b*other.b
        return new

    def __truediv__(self,other):
        new=Fraccion()
        new.a=self.a*other.b
        new.b=self.b*other.a
        return new

    def __repr__(self):
        entero=self.a//self.b
        if entero>0:
            resto=self.a%self.b
            if resto>0:
                return "{0} {1}/{2}".format(entero,resto,self.b)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.a,self.b)

    def a_numero(self):
        return self.a/self.b

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