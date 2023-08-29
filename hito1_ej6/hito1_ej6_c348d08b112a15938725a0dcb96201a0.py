#Ordenar tres números
   n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))
n3 = int(input("Ingrese un número: "))

if n1 >= n2 >= n3 :
    print("{},{},{}".format(n3, n2, n1))

if n3 >= n2 >= n1 :
    print("{},{},{}".format(n1, n2, n3))

if n2 >= n1 >= n3 :
    print("{},{},{}".format(n3, n1, n2))

if n2 >= n3 >= n1 :
    print("{},{},{}".format(n1, n3, n2))

if n1 >= n3 >= n2 :
    print("{},{},{}".format(n2, n3, n1))

if n3 >= n1 >= n2 :
    print("{},{},{}".format(n2, n1, n3))              