n1 = int(input("Ingresa el primer numero"))
n2 = int(input("Ingresa el primer numero"))
n3 = int(input("Ingresa el primer numero"))


if n1 < n2 < n3:
    print("El orden de los numero colocados es el siguente: ", n1, n2, n3)
if n3 < n2 < n1:
    print("El orden de los numero colocados es el siguente: ", n3, n2, n1)
if n2 < n3 < n1:
    print("El orden de los numero colocados es el siguente: ", n2, n3, n1)
if n2 < n1 < n3:
    print("El orden de los numero colocados es el siguente: ", n2, n1, n3)
if n1 < n3 < n2:
    print("El orden de los numero colocados es el siguente: ", n1, n3, n2)
if n3 < n1 < n2:
    print("El orden de los numero colocados es el siguente: ", n3, n1, n2)
if n1 == n2 or n2 ==n3 or n3 ==n1:
    print("ingrese valores distintos")