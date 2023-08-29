def amigos(a, b):
    if (a == b or a <= 2 or b <= 2):
        return False

    sum1 = 0
    sum2 = 0

    for i in range(1, a):
        if (i % a == 0):
            sum1 += i
    for i in range(1, b):
        if (i % b == 0):
            sum2 += i
    
    return sum1 == sum2