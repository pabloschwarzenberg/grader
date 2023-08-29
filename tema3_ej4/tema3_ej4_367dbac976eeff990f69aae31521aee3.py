class Fraccion:
    def _init_(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def _add_(self, other):
        if isinstance(other, Fraccion):
            num_sum = (self.num * other.den) + (other.num * self.den)
            den_sum = self.den * other.den
            return Fraccion(num_sum, den_sum)
        else:
            raise TypeError("La operación de suma solo es válida para objetos de la clase Fraccion.")

    def _sub_(self, other):
        if isinstance(other, Fraccion):
            num_diff = (self.num * other.den) - (other.num * self.den)
            den_diff = self.den * other.den
            return Fraccion(num_diff, den_diff)
        else:
            raise TypeError("La operación de resta solo es válida para objetos de la clase Fraccion.")

    def _mul_(self, other):
        if isinstance(other, Fraccion):
            num_prod = self.num * other.num
            den_prod = self.den * other.den
            return Fraccion(num_prod, den_prod)
        else:
            raise TypeError("La operación de multiplicación solo es válida para objetos de la clase Fraccion.")

    def _truediv_(self, other):
        if isinstance(other, Fraccion):
            num_div = self.num * other.den
            den_div = self.den * other.num
            return Fraccion(num_div, den_div)
        else:
            raise TypeError("La operación de división solo es válida para objetos de la clase Fraccion.")

    def _repr_(self):
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
    f = input("Ingresa la primera fracción [a/b]: ")
    f = f.split("/")
    f1 = Fraccion(int(f[0]), int(f[1]))

    f = input("Ingresa la segunda fracción [c/d]: ")
    f = f.split("/")
    f2 = Fraccion(int(f[0]), int(f[1]))

    print("La suma es", f1 + f2)
    print("La resta es", f1 - f2)
    print("La multiplicación es", f1 * f2)
    print("La división es", f1 / f2)         