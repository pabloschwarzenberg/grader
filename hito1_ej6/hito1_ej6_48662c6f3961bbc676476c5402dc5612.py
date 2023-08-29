#Ordenar tres números
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print("{},{},{}".format(n3, n2, n1))
    else:
        print("{},{},{}".format(n2, n3, n1))

elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print("{},{},{}".format(n3, n1, n2))
    else:
        print("{},{},{}".format(n1, n3, n1))

else:
    if n1 >= n2:
        print("{},{},{}".format(n2, n1, n3))
    else:
        print("{},{},{}".format(n1, n2, n3))