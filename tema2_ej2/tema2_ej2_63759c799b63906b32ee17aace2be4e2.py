def amigos(a,b):
    k = 1
    i = 0
    t = 1
    o = 0
    while a >= k:
        if a % k == 0:
            i = i + k
        k+=1
    while b >= t:
        if b % t == 0:
            o = o + t
        t+=1
    if a!=b and i==o:
        return True
    elif a == b:
        return False
    else:
        return False