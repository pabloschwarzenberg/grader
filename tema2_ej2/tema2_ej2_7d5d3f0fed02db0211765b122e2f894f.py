# completa el código de la función
def amigos(a,b):
    i = 1
    div = 0
    sum = 0
    i2 = 1
    div2 = 0
    sum2 = 0
    while i < a:
        div = a % i
        if div == 0:
            sum += i
        i += 1

    while i2 < b:
        div = b % i2
        if div == 0:
            sum2 += i2
        i2 += 1

    if sum == b and sum2 == a:
        return True
    else:
        return False
           