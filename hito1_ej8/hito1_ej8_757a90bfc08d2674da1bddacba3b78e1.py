#Descomponer un número
numero = int(input("ingrese un numero de hasta 4 dijitos"))
mil = ((numero)//1000)
cien = ((numero)//100)%10
diez = ((numero)//10)%10
unidad = ((numero)//1)%10
print("%dM + %dC + %dD + %dU" %(mil, cien, diez, unidad))