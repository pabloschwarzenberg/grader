def numero_perfecto(a):
    suma = 0
    for i in range(1, a):
        if (a % (i) == 0):
            suma += (i)
    if a == suma:
        return True
    else:
        return False

a = 6
if numero_perfecto(a):
    print("%s es un numero perfecto" % a)
else:
    print("%s NO es un numero perfecto" % a)


