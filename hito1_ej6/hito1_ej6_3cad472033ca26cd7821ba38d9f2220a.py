#Ordenar tres números
U = int(input("INTRODUZCA EL PRIMER NUMERO: "))
D = int(input("INTRODUZCA EL SEGUDNO NUMERO: "))
T = int(input("INTRODUZCA EL TERCER NUMERO: "))

A = min(U,D,T)
C = max(U,D,T)
Z = (U + D + T) - A - C

print ('Los numeros ordenados son: {}, {}, {}'.format(A, Z, C))