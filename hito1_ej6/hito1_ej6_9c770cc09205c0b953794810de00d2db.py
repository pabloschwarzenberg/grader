#Ordenar tres números
x=int(input("Favor digite el primer numero: "))
y=int(input("Favor digite el segundo numero: "))
z=int(input("Favor digite el terecer numero: "))
a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print("Los numeros ordenados quedan de la sgte manera: {},{},{}".format(a,b,c))