class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def simplificar(self):
        mcd = self.mcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd
    
    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def __add__(self, other):
        if isinstance(other, Fraccion):
            numerador = self.numerador * other.denominador + self.denominador * other.numerador
            denominador = self.denominador * other.denominador
            resultado = Fraccion(numerador, denominador)
            resultado.simplificar()
            return resultado
        else:
            raise ValueError("Invalid operand type. Expected Fraccion.")
    
    def __sub__(self, other):
        if isinstance(other, Fraccion):
            numerador = self.numerador * other.denominador - self.denominador * other.numerador
            denominador = self.denominador * other.denominador
            resultado = Fraccion(numerador, denominador)
            resultado.simplificar()
            return resultado
        else:
            raise ValueError("Invalid operand type. Expected Fraccion.")
    
    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            numerador = self.numerador * other.denominador
            denominador = self.denominador * other.numerador
            resultado = Fraccion(numerador, denominador)
            resultado.simplificar()
            return resultado
        else:
            raise ValueError("Invalid operand type. Expected Fraccion.")

# Ejemplo de uso
f1 = Fraccion(1, 2)
f2 = Fraccion(3, 4)

f3 = f1 + f2
print(f3.numerador, f3.denominador)  # Output: 5, 4

f4 = f1 - f2
print(f4.numerador, f4.denominador)  # Output: -1, 4

f5 = f1 / f2
print(f5.numerador, f5.denominador)  # Output: 2, 3
