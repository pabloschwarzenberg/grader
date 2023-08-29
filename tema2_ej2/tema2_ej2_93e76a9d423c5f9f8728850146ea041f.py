# completa el código de la función
def amigos(a,b):
    n = 1
    m = 1
    ia = 0
    ib = 0
    while a > n:
        if a % n == 0:
            ia = n + ia
        n = n + 1
    while b > m:
        if b % m == 0:
            ib=m+ib
        m = m + 1
    if ia==b and ib==a:
        return True
    else:
            return False
print(amigos(220,284))