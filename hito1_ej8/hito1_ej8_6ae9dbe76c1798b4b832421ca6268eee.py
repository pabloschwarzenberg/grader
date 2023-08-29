## BLOQUE PRINCIPAL:
## Entrada de datos:
numero = int(input("Ingresa un número de 4 cifras: "))

##Proceso:
unidades= numero%10
numero = numero//10

decenas = numero%10
numero = numero//10

centenas = numero%10
numero = numero//10

unidadesMil = numero%10

##salida de datos:
print((str(unidadesMil)+("M+"))+(str(centenas)+("C+"))+(str(decenas)+("D+"))+(str(unidades)+("U")))