#Ordenar tres números
x=int(input("Ingresar el primer numero: "))
y=int(input("Ingresar el segundo numero: "))
z=int(input("ingresar el tercer numero: "))
a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print("Los numero se ordenan de la siguiente manera: {},{},{}".format(a,b,c))