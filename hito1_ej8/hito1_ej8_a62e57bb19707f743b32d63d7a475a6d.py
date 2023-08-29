#Programa que separa un número de 4 cifras a umil, centenas, decenas, unidad.
n = int(input("Ingrese un numero de cuatro digitos:   "))

unidad = n%10

n = n//10

decenas = n%10

n = n//10

centenas = n%10

n = n//10

umil = n

print(umil,"M +",centenas,"C +",decenas,"D +",unidad,"U")