#Descomponer un número
numero = int(input("ingrese numero de 4 digitos: "))
      
unidades = numero%10
numero = numero//10
decenas = numero%10
numero = numero//10
centenas = numero%10
numero = numero//10
UnidadMil = numero%10

print(UnidadMil,"M +",centenas,"C +",decenas,"D +",unidades,"U")