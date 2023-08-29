#Ordenar tres números
a=int(input("Ingrese un número: "))
b=int(input("Ingrese un segundo número: "))
c=int(input("ingrese un tercer número: "))
d=min(a,b,c)
f=max(a,b,c)
g=(a+b+c)-d-f
print("Los números ordenados de menor a mayor son:", (d, g, f))