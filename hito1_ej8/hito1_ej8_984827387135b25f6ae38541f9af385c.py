#Descomponer un número
numeros=int(input("Introduce el número: "))
umil = int (numeros / 1000)
a = numeros % 1000
centenas = int (a / 100)
a = a % 100
decenas = int (a / 10)
unidades = int (numeros%10)
print("La descomposicion es",umil,"M +",centenas,"C +",decenas,"D +",unidades,"U")
# por favor escribe aquí tu función
def es_primo(a):
    if a > 1:
        for i in range(2,a):
            if a % i == 0:
                return False
            return True
    else:
        return False