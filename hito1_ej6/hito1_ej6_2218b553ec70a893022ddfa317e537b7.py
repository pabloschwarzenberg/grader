#Ordenar tres números
A = eval(input("Ingresa tu primer numero: "))
B = eval(input("Ingresa tu segundo numero: "))
C = eval(input("Ingresa tu tercer numero: "))
D = min (A,B,C)
E = max(A,B,C)
F = ((A+B+C)-D-E)

print("{},{},{}" .format(D,F,E))     