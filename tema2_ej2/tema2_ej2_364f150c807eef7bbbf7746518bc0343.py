# completa el código de la función
def amigos(a,b):
    la = []
    lb = []
    ca = a
    cb = b
    while ca != 0:
        if a % ca == 0:
            la.append(ca)
            pass
        else:
            pass
        ca = ca - 1
    pass
    while cb != 0:
        if b % cb == 0:
            lb.append(cb)
            pass
        else:
            pass
        cb = cb - 1
    pass
    la.remove(a)
    lb.remove(b)
    vfa = sum(la)
    vfb = sum(lb)  
    if vfa == b and vfb == a:
        return True
    else:
        return False