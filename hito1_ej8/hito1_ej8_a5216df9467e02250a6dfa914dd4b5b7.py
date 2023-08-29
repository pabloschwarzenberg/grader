#Descomponer un número
numero = int(input("ingrese un numero de hasta 4 digitos"))
milesima = ((numero)//1000)
centesima = ((numero)//100)%10
decima = ((numero)//10)%10
unidad = ((numero)//1)%10
print("%dM + %dC + %dD + %dU" %(milesima, centesima, decima, unidad))