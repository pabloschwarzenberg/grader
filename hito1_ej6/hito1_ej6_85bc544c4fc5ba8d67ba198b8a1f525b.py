#Ordenar tres números
A = int(input("Ingrese el primer numero:"))
B = int(input("Ingrese el segundo numero:"))
C = int(input("Ingrese el tercer numero:"))

Z = min(A,B,C)
X = max(A,B,C)
Y = ((A+B+C)-Z-X)

print("Los numeros ordenados de menor a mayor son:{},{},{}".format(Z,Y,X))