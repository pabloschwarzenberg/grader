#Ordenar tres números
n1 = eval(input("ingrese el primer numero: "))
n2 = eval(input("ingrese el segundo numero: "))
n3 = eval(input("ingrese el tercer numero: "))

if (n1 < n2) and (n1 < n3) and (n2 < n3):
    print("numeros ordenados de menor a mayor: {0}, {1}, {2}".format(n1, n2, n3))
elif (n1 == n2) and (n1 == n3):
    print("numeros ordenados de menor a mayor: {0}, {1}, {2}".format(n1, n2, n3))
elif (n1 == n2) and (n1 < n3):
    print("numeros ordenados de menor a mayor: {0}, {1}, {2}".format(n1, n2, n3))
elif (n1 == n2) and (n1 > n3):
    print("numeros ordenados de menor a mayor: {0}, {1}, {2}".format(n3, n1, n2))
elif (n1 == n3) and (n2 < n3):
    print("numeros ordenados de menor a mayor: {0}, {1}, {2}".format(n2, n3, n1))
elif (n1 == n3) and (n2 > n3):
    print("numeros ordenados de menor a mayor: {0}, {1}, {2}".format(n1, n3, n2))
elif (n2 == n3) and (n1 < n2):
    print("numeros ordenados de menor a mayor: {0}, {1}, {2}".format(n1, n2, n3))
elif (n2 == n3) and (n1 > n2):
    print("numeros ordenados de menor a mayor: {0}, {1}, {2}".format(n2, n3, n1))
elif (n1 > n2) and (n2 < n3) and (n1 < n3):
    print("numeros ordenados de menor a mayor: {0}, {1}, {2}".format(n2, n1, n3))
elif (n1 < n2) and (n1 < n3) and (n2 > n3):
    print("numeros ordenados de menor a mayor: {0}, {1}, {2}".format(n1, n3, n2))
elif (n1 < n2) and (n1 > n3) and (n2 > n3):
    print("numeros ordenados de menor a mayor: {0}, {1}, {2}".format(n3, n1, n2))
elif (n1 > n2) and (n1 > n3) and (n2 < n3):
    print("numeros ordenados de menor a mayor: {0}, {1}, {2}".format(n2, n3, n1))
else:
    print("numeros ordenados de menor a mayor: {0}, {1}, {2}".format(n3, n2, n1))