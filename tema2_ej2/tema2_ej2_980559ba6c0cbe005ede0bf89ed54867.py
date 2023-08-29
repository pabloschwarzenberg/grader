# completa el código de la función
def amigos(a,b):
    p = []
    for i in range(1,a+1):
        if a % i == 0:
            p.append(i)

    d = []
    for i in range(1,b+1):
        if b % i == 0:
            d.append(i)
    n = sum(p) - a
    m = sum(d) - b
    if n == b and m == a:
        return True
    else:
        return False