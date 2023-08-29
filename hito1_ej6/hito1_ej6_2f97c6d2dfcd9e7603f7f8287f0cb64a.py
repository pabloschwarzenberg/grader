#Ordenar tres números
A = []

n1 = int(input("ingrese el primer numero"))
n2 = int(input("ingrese el segundo numero"))
n3 = int(input("Ingrese el tercer numero: "))

A.append(n1)
A.append(n2)
A.append(n3)

A.sort()

print(A)