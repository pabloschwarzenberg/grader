class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __truediv__(self, other):
        new_num = self.num/(1/other.den)
        new_den = self.den/(1/other.num)
        return Fraccion(new_num, new_den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraccion(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraccion(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraccion(new_num, new_den)

    def repr(self):
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
      f=input("Ingresa la primera fracion [a/b]: ")
      f=f.split("/")
      f1=Fraccion(int(f[0]),int(f[1]))
      f=input("Ingresa la segunda fraccion [c/d]: ")
      f=f.split("/")
      f2=Fraccion(int(f[0]),int(f[1]))
      print("La suma es ", f1+f2)
      print("La resta es ", f1-f2)
      print("La multiplicación es ", f1*f2)
      print("La división es ", f1/f2)
         