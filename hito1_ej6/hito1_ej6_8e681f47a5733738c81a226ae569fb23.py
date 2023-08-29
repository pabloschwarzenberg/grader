#Ordenar tres números
x = int(input("Escribir el primer numero: "))
y = int(input("Escribir el segundo numero: "))
z = int(input("Escribir el tercer numero: "))
a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print("Los nros son: {}, {}, {}".format(a,b,c))