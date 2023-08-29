# completa el código de la función
def amigos(a,b):
    x1 = 0
    m1 = a
    r1 = 1
    while r1 < m1:
        n1 = m1
        z1 = int(m1%r1)
        if z1 == 0:
            x1 = x1 + r1
        r1 = r1+1
    x2 = 0
    m2 = b
    r2 = 1
    while r2 < m2:
        n2 = m2
        z2 = int(m2%r2)
        if z2 == 0:
            x2 = x2 + r2
        r2 = r2+1
    
    if x1 == b and x2 == a:
        return True
    else: return False
    
a = 220
b = 284
print(amigos(a,b))
         