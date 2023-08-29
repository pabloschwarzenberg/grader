class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        if isinstance(other, Fraccion):
            num = self.num * other.den + other.num * self.den
            den = self.den * other.den
            return Fraccion(num, den)
        else:
            raise TypeError("Se requiere un objeto de la clase Fraccion para realizar la suma.")

    def __sub__(self, other):
        if isinstance(other, Fraccion):
            num = self.num * other.den - other.num * self.den
            den = self.den * other.den
            return Fraccion(num, den)
        else:
            raise TypeError("Se requiere un objeto de la clase Fraccion para realizar la resta.")

    def __mul__(self, other):
        if isinstance(other, Fraccion):
            num = self.num * other.num
            den = self.den * other.den
            return Fraccion(num, den)
        else:
            raise TypeError("Se requiere un objeto de la clase Fraccion para realizar la multiplicación.")

    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            num = self.num * other.den
            den = self.den * other.num
            return Fraccion(num, den)
        else:
            raise TypeError("Se requiere un objeto de la clase Fraccion para realizar la división.")

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
    print("La suma es", f1 + f2)
    print("La resta es", f1 - f2)
    print("La multiplicación es", f1 * f2)
    print("La división es", f1 / f2)
