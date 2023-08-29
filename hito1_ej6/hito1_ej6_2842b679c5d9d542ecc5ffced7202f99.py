#Ordenar tres números
n1=int(input("Escriba el primer número: "))
n2=int(input("Escriba el segundo número: "))
n3=int(input("Escriba el tercer número: "))

a=min(n1, n2, n3)
c=max(n1, n2, n3)
b=(n1+n2+n3)-a-c

print("Los numeros ordenados son: ", (a, b, c))