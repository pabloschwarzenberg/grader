class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraccion(other, 1)
        nuevo_num = self.num * other.den + self.den * other.num
        nuevo_den = self.den * other.den
        return Fraccion(nuevo_num, nuevo_den)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraccion(other, 1)
        nuevo_num = self.num * other.den - self.den * other.num
        nuevo_den = self.den * other.den
        return Fraccion(nuevo_num, nuevo_den)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraccion(other, 1)
        nuevo_num = self.num * other.num
        nuevo_den = self.den * other.den
        return Fraccion(nuevo_num, nuevo_den)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraccion(other, 1)
        nuevo_num = self.num * other.den
        nuevo_den = self.den * other.num
        return Fraccion(nuevo_num, nuevo_den)

    def __repr__(self):
        if self.den == 1:
            return str(self.num)
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

    print("La suma es", f1 + f2)
    print("La resta es", f1 - f2)
    print("La multiplicación es", f1 * f2)
    print("La división es", f1 / f2)

         