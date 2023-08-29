#Ordenar tres números
a=int(input("Escriba el primer numero entero:"))
b=int(input("Escriba el segundo numero entero:"))
c=int(input("Escriba el tercero numero entero:"))


x = min(a,b,c)
y = max(a,b,c)
z = (a+b+c)-x-y

print("Los numeros ordenados de menor a mayor son: {}, {}, {}.".format(x,z,y))