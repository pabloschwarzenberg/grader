#Ordenar tres números
x=int(input("Ingrese primer número:"))
y=int(input("Ingrese segundo número:"))
z=int(input("Ingrese tercer número:"))
a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print("los números son: {},{},{}".format(a,b,c))   