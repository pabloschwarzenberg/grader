#Ordenar tres números
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

nMinimo = min(n1,n2,n3)
nMaximo = max(n1,n2,n3)

nMedio = (n1+n2+n3) - nMinimo - nMaximo

print(nMinimo , ", " , nMedio , ", " , nMaximo)
