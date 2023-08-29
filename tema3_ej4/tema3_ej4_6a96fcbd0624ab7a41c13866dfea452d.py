class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        # Suma de fracciones: a/b + c/d = (a*d + b*c) / (b*d)
        nuevo_num = self.num * other.den + self.den * other.num
        nuevo_den = self.den * other.den
        return Fraccion(nuevo_num, nuevo_den)

    def __sub__(self, other):
        # Resta de fracciones: a/b - c/d = (a*d - b*c) / (b*d)
        nuevo_num = self.num * other.den - self.den * other.num
        nuevo_den = self.den * other.den
        return Fraccion(nuevo_num, nuevo_den)

    def __mul__(self, other):
        # Multiplicación de fracciones: a/b * c/d = (a*c) / (b*d)
        nuevo_num = self.num * other.num
        nuevo_den = self.den * other.den
        return Fraccion(nuevo_num, nuevo_den)

    def __truediv__(self, other):
        # División de fracciones: a/b / c/d = (a*d) / (b*c)
        nuevo_num = self.num * other.den
        nuevo_den = self.den * other.num
        return Fraccion(nuevo_num, nuevo_den)

    def __repr__(self):
        entero = self.num // self.den
        resto = self.num % self.den

        if entero > 0:
            if resto > 0:
                return "{} {}/{}".format(entero, resto, self.den)
            else:
                return str(entero)
        else:
            return "{}/{}".format(self.num, self.den)

    def a_numero(self):
        return self.num / self.den


if __name__ == "__main__":
    f = input("Ingresa la primera fraccion [a/b]: ")
    f = f.split("/")
    f1 = Fraccion(int(f[0]), int(f[1]))

    f = input("Ingresa la segunda fraccion [c/d]: ")
    f = f.split("/")
    f2 = Fraccion(int(f[0]), int(f[1]))

    print("La suma es", f1.__add__(f2))
    print("La resta es", f1.__sub__(f2))
    print("La multiplicación es", f1.__mul__(f2))
    print("La división es", f1.__truediv__(f2))
