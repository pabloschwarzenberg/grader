class Fracción:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
        mcd = self.calcular_mcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    def calcular_mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def sumar(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador + otra_fraccion.numerador * self.denominador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        resultado = Fracción(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def restar(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador - otra_fraccion.numerador * self.denominador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        resultado = Fracción(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def dividir(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador
        nuevo_denominador = self.denominador * otra_fraccion.numerador
        resultado = Fracción(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado


# Ejemplo de uso
fraccion1 = Fracción(3, 4)
fraccion2 = Fracción(1, 2)

resultado_suma = fraccion1.sumar(fraccion2)
print(f"Suma: {resultado_suma.numerador}/{resultado_suma.denominador}")

resultado_resta = fraccion1.restar(fraccion2)
print(f"Resta: {resultado_resta.numerador}/{resultado_resta.denominador}")

resultado_division = fraccion1.dividir(fraccion2)
print(f"División: {resultado_division.numerador}/{resultado_division.denominador}")
