#Descomponer un número
numero = int(input('Ingrese un número de 4 cifras: '))

U = (numero%10)
D = (numero%100)//10
C = (numero//100)%10
M = numero//1000

print(f"{M}M {C}C {D}D {U}U")