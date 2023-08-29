def numero_perfecto(a):
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
    if vf == a:
        return True
    else:
        return False