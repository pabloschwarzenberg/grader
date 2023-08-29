class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        r = Fraccion(0, 0)
        r.num = self.num * other.den + other.num * self.den
        r.den = self.den * other.den
        return r

    def __sub__(self, other):
        r = Fraccion(0, 0)
        r.num = self.num * other.den - other.num * self.den
        r.den = self.den * other.den
        return r

    def __mul__(self, other):
        r = Fraccion(0, 0)
        r.num = self.num * other.num
        r.den = self.den * other.den
        return r

    def __truediv__(self, other):
        r = Fraccion(0, 0)
        r.num = self.num * other.den
        r.den = self.den * other.num
        return r

    def __float__(self):
        return float(self.num) / float(self.den)

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

if __name__ == "__main__":
    re1 = Fraccion(3, 4)
    im1 = Fraccion(2, 3)
    ro1 = Fraccion(5, 6)

    print("re1 =", re1)
    print("im1 =", im1)
    print("ro1 =", ro1)

    if float(re1) != float(ro1):
        print("re1 y ro1 no son iguales")
    else:
        print("re1 y ro1 son iguales")

    if float(im1) != float(ro1):
        print("im1 y ro1 no son iguales")
    else:
        print("im1 y ro1 son iguales")