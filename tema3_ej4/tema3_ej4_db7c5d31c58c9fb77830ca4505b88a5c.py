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
    
    def __add__(self, otra_fraccion):
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        nuevo_numerador = (self.numerador * otra_fraccion.denominador) + (otra_fraccion.numerador * self.denominador)
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado
    
    def __sub__(self, otra_fraccion):
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        nuevo_numerador = (self.numerador * otra_fraccion.denominador) - (otra_fraccion.numerador * self.denominador)
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado
    
    def __truediv__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador
        nuevo_denominador = self.denominador * otra_fraccion.numerador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado
