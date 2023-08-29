#Descomponer un número
numeros=int(input("Introduce el número: "))
umil = int (numeros / 1000)
a = numeros % 1000
centenas = int (a / 100)
a = a % 100
decenas = int (a / 10)
unidades = int (numeros%10)
print("La descomposicion es",umil,"M +",centenas,"C +",decenas,"D +",unidades,"U")