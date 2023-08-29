class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        else:
            return False

if __name__ == "__main__":
    cuenta = Cuenta("123456789", 1000)
    print(cuenta.girar(500))  # True
    print(cuenta.saldo)  # 500
    print(cuenta.girar(1000))  # False
    print(cuenta.saldo)  # 500


# clase vector 3d

from math import sqrt

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            x_sum = self.x + other.x
            y_sum = self.y + other.y
            z_sum = self.z + other.z
            return Vector(x_sum, y_sum, z_sum)
        else:
            raise TypeError("Unsupported operand type.")

def suma_vectores(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return v1 + v2
    else:
        raise TypeError("Unsupported operand type.")

if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print(v1.norma())  # 3.7416573867739413
    print(suma_vectores(v1, v2))  # <__main__.Vector object at 0x000001>
    print(v1 + v2)  # <__main__.Vector object at 0x000002>



# clase fraccion 


class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __add__(self, other):
        if isinstance(other, Fraccion):
            numerador_suma = self.num * other.den + other.num * self.den
            denominador_suma = self.den * other.den
            return Fraccion(numerador_suma, denominador_suma)
        else:
            raise TypeError("Unsupported operand type.")

    def __sub__(self, other):
        if isinstance(other, Fraccion):
            numerador_resta = self.num * other.den - other.num * self.den
            denominador_resta = self.den * other.den
            return Fraccion(numerador_resta, denominador_resta)
        else:
            raise TypeError("Unsupported operand type.")

    def __mul__(self, other):
        if isinstance(other, Fraccion):
            numerador_mul = self.num * other.num
            denominador_mul = self.den * other.den
            return Fraccion(numerador_mul, denominador_mul)
        else:
            raise TypeError("Unsupported operand type.")

    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            numerador_div = self.num * other.den
            denominador_div = self.den * other.num
            return Fraccion(numerador_div, denominador_div)
        else:
            raise TypeError("Unsupported operand type.")

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
