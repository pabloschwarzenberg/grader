print("Ingresa 3 números enteros")

x = int(input("Ingresa un número"))
y = int(input("Ingresa un segundo número"))
z = int(input("Ingresa un tercer número"))


if x < y < z:
    print(str(x) + "," + str(y) + "," + str(z))
elif x < z < y:
    print(str(x) + "," + str(z) + "," + str(y))
elif y < x < z:
    print(str(y) + "," + str(x) + "," + str(z))
elif y < z < x:
    print(str(y) + "," + str(z) + "," + str(x))
elif z < y < x:
    print(str(z) + "," + str(y) + "," + str(x))
elif z < x < y:
    print(str(z) + "," + str(x) + "," + str(y))
elif x == y < z:
    print(str(x) + "," + str(y) + "," + str(z))
elif x == z < y:
    print(str(x) + "," + str(z) + "," + str(y))
elif x < y == z:
    print(str(x) + "," + str(y) + "," + str(z))
elif y < x == z:
    print(str(y) + "," + str(x) + "," + str(z))
elif z < x == y:
    print(str(z) + "," + str(x) + "," + str(y))
elif x == y == z:
    print(str(x) + "," + str(y) + "," + str(z))
elif y == z < x:
    print(str(y) + "," + str(z) + "," + str(x))