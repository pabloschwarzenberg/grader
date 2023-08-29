def amigos(a,b):
    sumdiva = 0
    for n in range(1, a):
        if a % n == 0:
            sumdiva += n
    sumdivb = 0
    for n in range(1, b):
        if b % n == 0:
            sumdivb += n
            
    if sumdiva == b and sumdivb == a:
        return True
    else:
        return False


resp = amigos(2,2)
print(resp)