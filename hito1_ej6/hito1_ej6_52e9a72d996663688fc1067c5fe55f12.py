#Ordenar tres números
n1 = int(input("Ingrese el primer numero:"))
n2 = int(input("Ingrese el segundo numero:"))
n3 = int(input("Ingrese el tercer numero:"))

A = max(n1,n2,n3)
B = min(n1,n2,n3)
C = (n1+n2+n3) -A -B

print(B,",",C,",",A)