def amigos(a,b):
    sa = 0
    sb = 0
    ia = 1
    ib = 1
    while ia < a:
        if a%ia == 0:
            sa += ia
        ia += 1
    while ib < b:
        if b%ib == 0:
            sb += ib
        ib += 1
    if sa == b and sb== a:
        return True
    else:
        return False
try:
    na = int(input('numero a: '))
    nb = int(input('numero b: '))
    print(amigos(na,nb))
except:
    print('')
