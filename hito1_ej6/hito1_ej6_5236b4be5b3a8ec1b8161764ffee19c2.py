print("09. ORDENAR 3 NÚMEROS INGRESADOS.")
n1 = int(input("Ingrese Número 01 : "))
n2 = int(input("Ingrese Número 02 : "))
n3 = int(input("Ingrese Número 03 : "))
if (n1 > n2) and (n1 > n3):
    p = n1
    if n2 > n3:
        s = n2
        t = n3
    else:
        s = n3
        t = n2
elif n2 > n3:
    p = n2
    if n1 > n3:
        s = n1
        t = n3
    else:
        s = n3
        t = n1
else:
    p = n3
    if n1 > n2:
        s = n1
        t = n2
    else:
        s = n2
        t = n1
print("Ascendente  : ", t, " - ", s, " - ", p)