def amigos(a,b):
    divisoresa = 0
    divisoresb = 0
    for aa in range(1,a):
        if a % aa == 0:
            divisoresa += aa

    for bb in range(1,b):
        if b % bb == 0:
            divisoresb += bb

    if divisoresa == b and divisoresb == a:
        return True
    else:
        return False
           