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
        r = Fraccion(0, 0)
        r.num = self.num * other.den + other.num * self.den
        r.den = self.den * other.den
        return r

    def __sub__(self, other):
        r = Fraccion(0, 0)
        r.num = self.num * other.den - other.num * self.den
        r.den = self.den * other.den
        return r

    def __truediv__(self, other):
        r = Fraccion(0, 0)
        r.num = self.num * other.den
        r.den = self.den * other.num
        return r

    def __repr__(self):
        entero = self.num // self.den
        if entero > 0:
            resto = self.num % self.den
            return str(entero) + " " + str(resto) + "/" + str(self.den)
        else:
            return str(self.num) + "/" + str(self.den)

    def a_numero(self):
        return self.num / self.den

if __name__ == "__main__":
    f1 = Fraccion(1, 2)
    f2 = Fraccion(3, 4)

    suma = f1 + f2
    resta = f1 - f2
    producto = f1 * f2
    division = f1 / f2

    print(suma)  # Salida: 5/4
    print(resta)  # Salida: -1/4
    print(producto)  # Salida: 3/8
    print(division)  # Salida: 2/3
    print(f1.a_numero())  # Salida: 0.5
    print(f2.a_numero())  # Salida: 0.75
