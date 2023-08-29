#Descomponer un número
n = int(input("Ingrese un numero (max. 4 digitos): "))

M = n//1000
C = n % 1000
C = C//100
D = n % 100
D = D//10
U = n % 10
U = U//1

print("{0}M + {1}C + {2}D + {3}U".format(M, C, D, U))
