class Fraccion():
    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        if denominador == 0:
            raise Exception("El denominador no puede ser 0")
        self.denominador = int(denominador)

    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)

    def equivalente(self, otra: 'Fraccion') -> bool:
        return self.denominador == otra.denominador and self.numerador == otra.numerador

    def maximo_comun_divisor(self, a, b):
        temporal = 0
        while b != 0:
            temporal = b
            b = a % b
            a = temporal
        return a

    def minimo_comun_multiplo(self, a, b):
        return (a * b) / self.maximo_comun_divisor(a, b)

    """
    Operaciones
    """

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

    def inversa(self) -> 'Fraccion':
        return Fraccion(self.denominador, self.numerador)

    def potencia(self, exponente) -> 'Fraccion':
        return Fraccion(self.numerador ** exponente, self.denominador ** exponente)

    def simplifica(self) -> 'Fraccion':
        mcd = self.maximo_comun_divisor(self.numerador, self.denominador)
        return Fraccion(self.numerador / mcd, self.denominador / mcd)

    def a_mixta(self) -> 'FraccionMixta':
        return FraccionMixta.desde_impropia(self)

if __name__ == "__main__":
    f=input("Ingresa la primera fraccion [a/b]: ")
    f=f.split("/")
    f1=Fraccion(int(f[0]),int(f[1]))
    f=input("Ingresa la segunda fraccion [c/d]: ")
    f=f.split("/")
    f2=Fraccion(int(f[0]),int(f[1]))
    print("La suma es ",f1+f2)
    print("La resta es ",f1-f2)
    print("La multiplicación es ",f1*f2)
    print("La división es ",f1/f2)
         