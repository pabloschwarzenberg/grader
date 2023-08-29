#Ordenar tres números
x=int(input("ingres su primer valor: "))
y=int(input("ingrese su segundo valor: "))
z=int(input("ingrese su tercer valor: "))
a=min(x, y, z)
c=max(x, y, z)
b=(x++y+z)-a-c
print("los numeros ordenados de menor a mayor respectivamente es: {}, {}, {}". format(a, b, c))