#Ordenar tres números
n1=int(input("Ingrese el primer número: "))
n2=int(input("Ingrese el segundo número: "))
n3=int(input("Ingrese el tercer número: "))

maximo= max(n1,n2,n3)
minimo= min(n1,n2,n3)
medio= (n1+n2+n3)-maximo-minimo

print("Los números ordenados de menor a mayor son:",minimo,",",medio,",",maximo)