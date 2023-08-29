#Descomponer un número
N = int(input('ingrese un número de 4 dígitos'))

M = N//1000
N=N-1000*M
C = N//100
N=N-100*C
D = N//10
U = N-10*D

print(M,'M +',C,'C +',D,'D +',U,'U')