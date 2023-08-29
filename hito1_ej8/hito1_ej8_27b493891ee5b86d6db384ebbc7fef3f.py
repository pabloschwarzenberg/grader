#Descomponer un número
numero = int(input("Ingrese un número de hasta 4 dígitos: "))
n1 = numero // 10 ** 3 % 10
n2 = numero // 10 ** 2 % 10
n3 = numero // 10 ** 1 % 10
n4 = numero % 10

mil = str(n1) + "M"
centena = str(n2) + "C"
decena = str(n3) + "D"
unidad = str(n4) + "U"

if n1 == 0:
 print(centena,"+",decena,"+",unidad)
else:
 print(mil,"+",centena,"+",decena,"+",unidad)