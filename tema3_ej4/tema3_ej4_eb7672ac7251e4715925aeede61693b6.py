class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __mul__(self, other):
        r = Fraccion(0, 0)
        r.num = self.num * other.num
        r.den = self.den * other.den
        return r
    def __add__(self, other):
        if self.den==other.den:
            r = Fraccion(0,0)
            s = self.num + other.num
            r.num=s
            r.den=self.den
            return r
        else:
            r = Fraccion(0,0)
            if self.den>other.den:
                greater=self.den
            else:
                greater=other.den
            while True:
                if ((greater%self.den==0) and (greater%other.den==0)):
                    mcm=greater
                    break
                greater+=1
            x = greater/self.den
          
            s = (x*self.num) + other.num
            r.num=s
            r.den=greater
            return r

    def __sub__(self, other):
        if self.den==other.den:
            r = Fraccion(0,0)
            s = self.num - other.num
            r.num=s
            r.den=self.den
            return r
        else:
            r = Fraccion(0,0)
            if self.den>other.den:
                greater=self.den
            else:
                greater=other.den
            while True:
                if ((greater%self.den==0) and (greater%other.den==0)):
                    mcm=greater
                    break
                greater+=1
            x=greater/self.den
            s = x*self.num - other.num
            r.num=s
            r.den=mcm
            return r
    def __truediv__(self, other):
        r = Fraccion(0,0)
        r.num=self.num * other.den
        r.den=self.den * other.num
        return r

    def __repr__(self):
        entero = self.num // self.den
        if entero > 0:
            resto = self.num % self.den
            if resto > 0:
                return "{0} {1}/{2}".format(entero, resto, self.den)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.num, self.den)

    def a_numero(self):

        return self.num / self.den

if __name__ == "__main__":
    f = input("Ingresa la primera fraccion [a/b]: ")
    f = f.split("/")
    f1 = Fraccion(int(f[0]), int(f[1]))
    f = input("Ingresa la segunda fraccion [c/d]: ")
    f = f.split("/")
    f2 = Fraccion(int(f[0]), int(f[1]))
    print("La suma es ", (f1 + f2).a_numero())
    print("La resta es ",(f1 - f2).a_numero())
    print("La multiplicación es ", (f1 * f2).a_numero())
    print("La división es ", (f1 / f2).a_numero())


