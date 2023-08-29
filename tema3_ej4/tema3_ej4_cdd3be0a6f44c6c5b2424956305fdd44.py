class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        if denominador == 0:
            raise Exception("El denominador no puede ser 0")
        self.denominador = int(denominador)

    def suma(self, otra: 'Fraccion') -> 'Fraccion':
        mcm = self.minimo_comun_multiplo(self.denominador, otra.denominador)
        diferencia_self = mcm/self.denominador
        diferencia_otra = mcm/otra.denominador
        numerador_resultado = (diferencia_self*self.numerador) + \
            (diferencia_otra*otra.numerador)
        return Fraccion(numerador_resultado, mcm)

    def resta(self, otra: 'Fraccion') -> 'Fraccion':
        mcm = self.minimo_comun_multiplo(self.denominador, otra.denominador)
        diferencia_self = mcm/self.denominador
        diferencia_otra = mcm/otra.denominador
        numerador_resultado = (diferencia_self*self.numerador) - \
            (diferencia_otra*otra.numerador)
        return Fraccion(numerador_resultado, mcm)

    def producto(self, otra: 'Fraccion') -> 'Fraccion':
        return Fraccion(self.numerador*otra.numerador, self.denominador*otra.denominador)

    def cociente(self, otra: 'Fraccion') -> 'Fraccion':
        return Fraccion(self.numerador*otra.denominador, self.denominador*otra.numerador)