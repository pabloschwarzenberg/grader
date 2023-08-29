#Ordenar tres números
x=int(input("Ingrese el primer numero: "))
y=int(input("Ingrese el segundo numero: "))
z=int(input("Ingrese el terecer numero: "))
a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print("los numeros ordenados de menor a mayor son los siguiente: {},{},{}".format(a,b,c))