def amigos(a,b):
    cont1 = 1
    cont2 = 1
    for i in range(2, a):
        if a % i == 0:
            cont1 = cont1 + i
    for i in range(2, b):
        if b % i == 0:
            cont2 = cont2 + i
    if cont1 == b and cont2 == a:
        return True
    else:
        return False