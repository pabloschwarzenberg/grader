def amigos(a,b):
    s1 = 1
    s2 = 1
    for i in range (2,a):
        if(a%i == 0):
            s1 += i
    for i in range (2,b):
        if(b%i == 0):
            s2 += i
    if(s1 == b and s2 == a):
        return True
    else:
        return False