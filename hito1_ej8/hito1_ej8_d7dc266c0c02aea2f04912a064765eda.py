#Descomponer un número
N = int(input("Ingrese un número de 4 digitos: "))
x = N
M = x // 1000
x = x % 1000
C = x // 100
x = x % 100
D = x // 10
U = x % 10
print(M, "M" " +", C, "C" " +", D, "D" " +", U, "U")