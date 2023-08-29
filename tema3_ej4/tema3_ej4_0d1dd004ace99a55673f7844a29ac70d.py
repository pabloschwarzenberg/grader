class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra_fraccion):
        nuevo_numerador = (self.numerador * otra_fraccion.denominador) + (otra_fraccion.numerador * self.denominador)
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __sub__(self, otra_fraccion):
        nuevo_numerador = (self.numerador * otra_fraccion.denominador) - (otra_fraccion.numerador * self.denominador)
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __truediv__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador
        nuevo_denominador = self.denominador * otra_fraccion.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)


# Ejemplo de uso
fraccion_1 = Fraccion(1, 2)
fraccion_2 = Fraccion(3, 4)

resultado_suma = fraccion_1 + fraccion_2
resultado_resta = fracciin_1 - fraccion_2
resultado_division = fraccion_1 / fraccion_2

print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("División:", resultado_division)
