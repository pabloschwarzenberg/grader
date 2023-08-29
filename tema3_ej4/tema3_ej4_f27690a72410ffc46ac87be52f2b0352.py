class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador + self.denominador * otra_fraccion.numerador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __sub__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador - self.denominador * otra_fraccion.numerador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __truediv__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador
        nuevo_denominador = self.denominador * otra_fraccion.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)

# Ejemplo de uso
fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(3, 4)

# Suma de fracciones
resultado_suma = fraccion1 + fraccion2
print(f"Suma: {resultado_suma}")

# Resta de fracciones
resultado_resta = fraccion1 - fraccion2
print(f"Resta: {resultado_resta}")

# División de fracciones
resultado_division = fraccion1 / fraccion2
print(f"División: {resultado_division}")
