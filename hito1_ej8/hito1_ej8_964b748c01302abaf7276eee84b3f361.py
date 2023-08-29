#Descomponer un número
numero = int(input("ingrese un numero de hasta 4 cifras:"))
M = (numero//1000)%10
C = (numero//100)%10
D = (numero//10)%10
U = (numero//1)%10

print ("el siguiente numero", numero, "queda como:", M, "M+",C, "C+", D, "D +", U, "U")