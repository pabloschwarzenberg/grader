x=int(input("ingrese numero 1:"))
y=int(input("ingrese numero 2:"))
z=int(input("ingrese numero 3:"))
a=min(x, y, z)
c=max(x, y, z)
b=(x+y+z)-a-c
print("los numeros ordenados son: {},{},{}".format(a, b, c))