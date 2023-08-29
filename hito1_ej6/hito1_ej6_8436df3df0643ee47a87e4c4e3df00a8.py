x=int(input("escribe un numero entero: "))
y=int(input("escribe un otro numero entero: "))
z=int(input("escribe el utimo numero entero: "))

a = min(x,y,z)
c = max(x,y,z)
b = (x + y + z) - a - c

print("el orden de los numero es son: {}, {} y {}".format(a,b,c))