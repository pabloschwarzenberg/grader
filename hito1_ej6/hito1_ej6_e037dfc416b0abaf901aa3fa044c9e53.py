#Ordenar tres números
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a <= b:
    if a <= c:
        primero = a
        if b <= c:
            segundo = b
            tercero = c
        else:
            segundo = c
            tercero = b
    else:
        primero = c
        segundo = a
        tercero = b
else:
    if b<=c:
        primero = b
        if c <= a:
            segundo = c
            tercero = a
        else:
            segundo = a
            tercero = c
    else:
        primero = c
        segundo = b
        tercero = a

print(primero, ", ", segundo, ", ", tercero)
