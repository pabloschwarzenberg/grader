n1=eval(input("numero 1:" ))
n2=eval(input("numero 2:" ))
n3=eval(input("numero 3:" ))
if (n1 < n2 and n1 < n3):
    primero = n1
    if (n2 < n3):
        segundo = n2
        tercero = n3
    else:
        segundo = n3
        tercero = n2
else:
    if (n2 < n1 and n2 < n3):
        primero = n2
        if n1 < n3:
            segundo= n1
            tercero= n3
        else:
            segundo= n3
            tercero= n1
    else:
        if (n3 < n2 and n3 < n1):
            primero= n3
            if n2 < n1:
                segundo= n2
                tercero= n1
            else:
                segundo= n1
                tercero= n2
print("{},{},{}".format(primero,segundo,tercero))

