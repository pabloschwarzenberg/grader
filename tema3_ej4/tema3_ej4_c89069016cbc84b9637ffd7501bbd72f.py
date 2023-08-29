class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
        mcd = self.calcular_mcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    @staticmethod
    def calcular_mcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra_fraccion):
        nuevo_numerador = (self.numerador * otra_fraccion.denominador) + (otra_fraccion.numerador * self.denominador)
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def __sub__(self, otra_fraccion):
        nuevo_numerador = (self.numerador * otra_fraccion.denominador) - (otra_fraccion.numerador * self.denominador)
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def __truediv__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador
        nuevo_denominador = self.denominador * otra_fraccion.numerador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado
