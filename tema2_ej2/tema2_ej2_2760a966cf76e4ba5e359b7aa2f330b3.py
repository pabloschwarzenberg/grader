# completa el código de la función
def amigos(a,b):
    dv1 = 1
    m1 = 0
    while dv1 < a:
        if a % dv1 == 0:
            m1 = m1 + dv1
        dv1 += 1
    dv2 = 1
    m2 = 0
    while dv2 < b:
        if b % dv2 == 0:
            m2 = m2 + dv2
        dv2 += 1
    if (m2 == a) and (b == m1):
        return True
    else:
        return False           