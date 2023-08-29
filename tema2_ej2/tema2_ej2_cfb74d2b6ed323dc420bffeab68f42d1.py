def amigos(a,b):

    i = 0
    for n in range(1, a):
        if a % n == 0:
            i = i + n
    t = 0
    for n in range(1, b):
        if b % n == 0:
            t = t + n
    if i == b and t == a:
        return True
    else:
        return False
