#Descomponer un número
N = eval(input('Ingrese un número de hasta 4 dígitos: '))
M = (N // 1000) % 10
C = (N // 100) % 10
D = (N // 10) % 10
U = (N // 1) % 10
if N < 10:
    print(U,'U')
elif 10 <= N < 100:
    print(D,'D+',U,'U')
elif 100 <= N < 1000:
    print(C,'C+',D,'D+',U,'U')
elif 1000 <= N < 10000:
    print(M,'M+',C,'C+',D,'D+',U,'U')