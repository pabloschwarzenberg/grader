def amigos(a,b):
    divisor = 2
    while divisor < a :
        if a % divisor == 0 :
            m += divisor
        divisor = divisor + 1 
    if m == b :
        return True
    else :
        return False
    while divisor < b :
        if b % divisor == 0 :
            u += divisor
        divisor = divisor + 1
    if u == b :
        return True
    else :
        return False
