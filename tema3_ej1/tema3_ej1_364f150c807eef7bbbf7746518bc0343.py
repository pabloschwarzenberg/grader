# completa el código de la función
def suma_divisores(a):
    la = []
    ca = a
    while ca != 0:
        if a % ca == 0:
            la.append(ca)
            pass
        else:
            pass
        ca = ca - 1
    pass
    la.remove(a)
    vf = sum(la)
    if vf == 1:
        return (vf,True)
    else:
        return (vf,False)
