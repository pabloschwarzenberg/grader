#Ordenar tres números
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
x=min (a,b,c)
z=max (a,b,c)
y=(a+b+c)-x-z

print("{},{},{}".format(x,y,z))