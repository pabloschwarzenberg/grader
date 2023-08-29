class Fracción:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
        # Calcular el máximo común divisor utilizando el algoritmo de Euclides
        a = self.numerador
        b = self.denominador
        while b != 0:
            a, b = b, a % b

        # Simplificar la fracción dividiendo tanto el numerador como el denominador por el máximo común divisor
        self.numerador //= a
        self.denominador //= a

    def __add__(self, other):
        if isinstance(other, Fracción):
            # Encontrar un denominador común para las dos fracciones
            denominador_común = self.denominador * other.denominador

            # Realizar la suma de los numeradores con el denominador común
            numerador_suma = (self.numerador * other.denominador) + (other.numerador * self.denominador)

            # Crear una nueva fracción con la suma de los numeradores y el denominador común
            suma = Fracción(numerador_suma, denominador_común)
            suma.simplificar()
            return suma
        else:
            raise TypeError("Unsupported operand type.")

    def __sub__(self, other):
        if isinstance(other, Fracción):
            # Encontrar un denominador común para las dos fracciones
            denominador_común = self.denominador * other.denominador

            # Realizar la resta de los numeradores con el denominador común
            numerador_resta = (self.numerador * other.denominador) - (other.numerador * self.denominador)

            # Crear una nueva fracción con la resta de los numeradores y el denominador común
            resta = Fracción(numerador_resta, denominador_común)
            resta.simplificar()
            return resta
        else:
            raise TypeError("Unsupported operand type.")

    def __truediv__(self, other):
        if isinstance(other, Fracción):
            # Invertir la segunda fracción y multiplicarla por la primera
            inversa = Fracción(other.denominador, other.numerador)
            resultado = self * inversa
            resultado.simplificar()
            return resultado
        else:
            raise TypeError("Unsupported operand type.")

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


# Ejemplo de uso
f1 = Fracción(1, 2)
f2 = Fracción(3, 4)

# Sumar dos fracciones
suma = f1 + f2
print("Suma:", suma)

# Restar dos fracciones
resta = f1 - f2
print("Resta:", resta)

# Dividir dos fracciones
división = f1 / f2
print("División:", división)

            if resto>0:
                return "{0} {1}/{2}".format(entero,resto,self.den)
            else:
                return "{0}".format(entero)
        else:
            return "{0}/{1}".format(self.num,self.den)

    def a_numero(self):
        return self.num/self.den

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
         