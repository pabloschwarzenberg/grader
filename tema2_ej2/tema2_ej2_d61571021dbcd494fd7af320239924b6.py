# completa el código de la función
def amigos(a,b):
    a_l = []
    b_l = []
    for i in range(1, int(a/2) + 1):
        if a % i == 0:
            a_l.append(i)
    for x in range(1, int(b/2) + 1):
        if b % x == 0:
            b_l.append(x)
    if sum(b_l) == a and sum(a_l) == b:
        return True
    else:
        return False
           