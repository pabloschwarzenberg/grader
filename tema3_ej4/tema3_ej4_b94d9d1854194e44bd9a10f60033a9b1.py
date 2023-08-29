class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        if isinstance(other, Fraccion):
            num_sum = (self.num * other.den) + (other.num * self.den)
            den_sum = self.den * other.den
            return Fraccion(num_sum, den_sum)
        else:
            raise TypeError("La operaciÃ³n de suma solo es vÃ¡lida para objetos de la clase Fraccion.")

    def __sub__(self, other):
        if isinstance(other, Fraccion):
            num_diff = (self.num * other.den) - (other.num * self.den)
            den_diff = self.den * other.den
            return Fraccion(num_diff, den_diff)
        else:
            raise TypeError("La operaciÃ³n de resta solo es vÃ¡lida para objetos de la clase Fraccion.")

    def __mul__(self, other):
        if isinstance(other, Fraccion):
            num_prod = self.num * other.num
            den_prod = self.den * other.den
            return Fraccion(num_prod, den_prod)
        else:
            raise TypeError("La operaciÃ³n de multiplicaciÃ³n solo es vÃ¡lida para objetos de la clase Fraccion.")

    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            num_div = self.num * other.den
            den_div = self.den * other.num
            return Fraccion(num_div, den_div)
        else:
            raise TypeError("La operaciÃ³n de divisiÃ³n solo es vÃ¡lida para objetos de la clase Fraccion.")

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
    f = input("Ingresa la primera fracciÃ³n [a/b]: ")
    f = f.split("/")
    f1 = Fraccion(int(f[0]), int(f[1]))

    f = input("Ingresa la segunda fracciÃ³n [c/d]: ")
    f = f.split("/")
    f2 = Fraccion(int(f[0]), int(f[1]))

    print("La suma es", f1 + f2)
    print("La resta es", f1 - f2)
    print("La multiplicaciÃ³n es", f1 * f2)
    print("La divisiÃ³n es", f1 / f2)
