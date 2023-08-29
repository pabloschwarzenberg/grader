#Descomponer un número
n = eval(input("ingrese numero de 4 digitos: "))
unidades = n%10
n = n//10
decenas = n%10
n = n//10
centenas = n%10
n = n//10
unidad_mil = n%10

print(unidad_mil,"M +",centenas,"C +",decenas,"D +",unidades,"U")
            