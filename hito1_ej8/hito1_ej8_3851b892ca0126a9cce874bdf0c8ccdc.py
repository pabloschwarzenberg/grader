#Descomponer un número
numero = eval(input("ingrese numero de 4 digitos: "))
unidades = numero%10
numero = numero//10
decenas = numero%10
numero = numero//10
centenas = numero%10
numero = numero//10
unidad_mil = numero%10

print(unidad_mil,"M +",centenas,"C +",decenas,"D +",unidades,"U")   