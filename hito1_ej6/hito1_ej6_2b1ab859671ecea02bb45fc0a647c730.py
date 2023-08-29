#Ordenar tres números
#ingrese 
x=int(input("colocar el primer numero: "))
y=int(input("colocar segundo numero: "))
z=int(input("colocar tercer numero: "))

a=min(x, y, z)
c=max(x, y, z)
b=(x + y + z) - a - c
print("numeros ordenados: {},{},{}".format(a, b, c))
