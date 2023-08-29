z = int(input("ingrese un numero"))
x = int(input("ingrese un numero"))
c = int(input("ingrese un numero"))
if z <= x <= c:
    print("los numeros ordenados son:{},{},{}".format(z, x, c))
elif z <= c <= x:
    print("los numeros ordenados son:{},{},{}".format(z, c, x))
elif x <= z <= c:
    print("los numeros ordenados son:{},{},{}".format(x, z, c))
elif x <= c <= z:
    print("los numeros ordenados son:{},{},{}".format(x, c, z))
elif c <= z <= x:
    print("los numeros ordenados son:{},{},{}".format(c, z, x))
elif c <= x <= z:
    print("los numeros ordenados son:{},{},{}".format(c, x, z))