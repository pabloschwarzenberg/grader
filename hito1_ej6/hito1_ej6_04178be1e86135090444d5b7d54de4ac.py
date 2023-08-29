#Ordenar tres números de menor a mayor, separados por una coma.
n1=int(input("Ingrese primer numero : "))
n2=int(input("Ingrese segundo numero : "))
n3=int(input("Ingrese tercer numero : "))
a=min(n1,n2,n3)
c=max(n1,n2,n3)
b=(n1+n2+n3) - a - c
print("Los numeros ordenados de menor a mayor son : {} , {} , {}" .format(a,b,c))