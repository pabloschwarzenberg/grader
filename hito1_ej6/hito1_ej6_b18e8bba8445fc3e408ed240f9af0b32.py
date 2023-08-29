#Ordenar tres números
x=int(input("Ingrese el primer numero"))
y=int(input("Infrese el segundo numero"))
z=int(input("ingrese el tercer numero"))
a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print("Los numeros ordenados de menor a mayor son: {}, {}, {}".format(a,b,c))