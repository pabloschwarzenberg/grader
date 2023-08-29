class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
    def simplificar(self):
        gcd = self.mcd(self.numerador, self.denominador)
        self.numerador //= gcd
        self.denominador //= gcd
    
    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def __add__(self, other):
        if isinstance(other, Fraccion):
            denominador_comun = self.denominador * other.denominador
            numerador_suma = (self.numerador * other.denominador) + (other.numerador * self.denominador)
            resultado = Fraccion(numerador_suma, denominador_comun)
            resultado.simplificar()
            return resultado
        else:
            raise TypeError("La suma solo es válida para objetos de la clase Fraccion")
    
    def __sub__(self, other):
        if isinstance(other, Fraccion):
            denominador_comun = self.denominador * other.denominador
            numerador_resta = (self.numerador * other.denominador) - (other.numerador * self.denominador)
            resultado = Fraccion(numerador_resta, denominador_comun)
            resultado.simplificar()
            return resultado
        else:
            raise TypeError("La resta solo es válida para objetos de la clase Fraccion")
    
    def __truediv__(self, other):
        if isinstance(other, Fraccion):
            numerador_division = self.numerador * other.denominador
            denominador_division = self.denominador * other.numerador
            resultado = Fraccion(numerador_division, denominador_division)
            resultado.simplificar()
            return resultado
        else:
            raise TypeError("La división solo es válida para objetos de la clase Fraccion")
         
         if __name__ == "__main__":
    f1 = Fraccion(

