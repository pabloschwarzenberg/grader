#Ordenar tres números
a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))
c=int(input("Ingrese el tercer número: "))
minimo=min(a,b,c)
maximo=max(a,b,c)
x=(a+b+c)-minimo-maximo
print("Ordenados de menor a mayor:", minimo, ",", x, ",", maximo)