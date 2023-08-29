def multiplicacion(prim):
    mult = 1
    for i in prim:
        mult = mult*i
        if mult > num:
            return False
    return mult


num = int(input("numero: "))
div = []
prim = []
for i in range(2, num+1):
    if num%i == 0:
        div.append(i)
for i in div:
    for x in range(2, i):
        if i%x == 0:
            break
    else:
        prim.append(i)

multi = multiplicacion(prim)

if multi == num:
    for i in prim:
        print(i)
else:
    for i in prim:
        aux = prim
        aux.append(i)
        multi = multiplicacion(aux)
        if multi == num:
            aux.sort()
            break
        elif multi == False:
            aux.sort()
            aux.pop(0)
            break
    for i in aux:
        print(i)