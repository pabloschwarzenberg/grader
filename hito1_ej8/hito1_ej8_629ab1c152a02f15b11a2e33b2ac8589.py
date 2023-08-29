#Descomponer un número
numero = int(input("Ingrese el valor de un numero de 4 cifras: "))

unidades = numero%10
numero = numero//10

decenas = numero%10
numero = numero//10

centenas = numero%10
numero = numero//10

unidadesMil = numero%10

print(unidadesMil,'M +',centenas,'C +',decenas,'D +',unidades,'U')  