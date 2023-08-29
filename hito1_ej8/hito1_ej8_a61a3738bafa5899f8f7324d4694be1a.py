#Descomponer un número
print ("Introduce el número: ")
numero = int(input())

unidad_de_mil = numero // 1000

division = numero % 1000

centenas = division // 100

division= division % 100

decenas = division // 10

unidades = division % 10

print (unidad_de_mil,"M +",centenas,"C +",decenas,"D +",unidades,"U")
