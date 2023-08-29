class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, otro):
        if isinstance(otro, Fraccion):
            numerador = self.num * otro.den + otro.num * self.den
            denominador = self.den * otro.den
            return Fraccion(numerador, denominador)
        else:
            raise ValueError("El objeto pasado no es una fracción.")

    def __sub__(self, otro):
        if isinstance(otro, Fraccion):
            numerador = self.num * otro.den - otro.num * self.den
            denominador = self.den * otro.den
            return Fraccion(numerador, denominador)
        else:
            raise ValueError("El objeto pasado no es una fracción.")

    def __mul__(self, otro):
        if isinstance(otro, Fraccion):
            numerador = self.num * otro.num
            denominador = self.den * otro.den
            return Fraccion(numerador, denominador)
        else:
            raise ValueError("El objeto pasado no es una fracción.")

    def __truediv__(self, otro):
        if isinstance(otro, Fraccion):
            if otro.num != 0:
                numerador = self.num * otro.den
                denominador = self.den * otro.num
                return Fraccion(numerador, denominador)
            else:
                raise ZeroDivisionError("División por cero.")
        else:
            raise ValueError("El objeto pasado no es una fracción.")

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