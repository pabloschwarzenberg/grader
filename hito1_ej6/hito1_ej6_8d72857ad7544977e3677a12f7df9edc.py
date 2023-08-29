#Ordenar tres números
n1 = eval(input("Inserte el numero 1: " ))
n2 = eval(input("Inserte el numero 2: " ))
n3 = eval(input("Inserte el numero 3: " ))
if n1 < n2 and n1 < n3:
    a = n1
    if n2 < n3:
        b = n2
        c = n3
    else:
        b = n3
        c = n2
else:
    if n2 < n1 and n2 < n3:
        a = n2
        if n1 < n3:
            b = n1
            c = n3
        else:
            b = n3
            c = n1
    else:
        if n3 < n2 and n3 < n1:
            a = n3
            if n2 < n1:
                b = n2
                c = n1
            else:
                b = n1
                c = n2
print("{},{},{}".format(a,b,c))