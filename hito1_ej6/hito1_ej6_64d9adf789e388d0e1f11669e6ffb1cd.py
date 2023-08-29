#Ordenar tres números
n1=round(int(input("ingresa un numero: ")))
n2=round(int(input("ingresa un numero: ")))
n3=round(int(input("ingresa un numero: ")))
x=min(n1,n2,n3)
y=max(n1,n2,n3)
z=(n1+n2+n3)-x-y
print("{},{},{}".format(x,z,y))