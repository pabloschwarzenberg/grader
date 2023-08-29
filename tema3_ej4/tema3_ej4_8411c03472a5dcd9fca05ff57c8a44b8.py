class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        num_result = self.num * other.den + other.num * self.den
        den_result = self.den * other.den
        return Fraccion(num_result, den_result)

    def __sub__(self, other):
        num_result = self.num * other.den - other.num * self.den
        den_result = self.den * other.den
        return Fraccion(num_result, den_result)

    def __mul__(self, other):
        num_result = self.num * other.num
        den_result = self.den * other.den
        return Fraccion(num_result, den_result)

    def __truediv__(self, other):
        num_result = self.num * other.den
        den_result = self.den * other.num
        return Fraccion(num_result, den_result)

    def __repr__(self):
        entero = self.num // self.den
        resto = self.num % self.den
        if entero > 0:
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
    print("La multiplicacion es", f1 * f2)
    print("La division es", f1 / f2)