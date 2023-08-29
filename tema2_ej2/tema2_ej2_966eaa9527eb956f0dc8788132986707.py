# completa el código de la función
def amigos(a,b):
    div1 = []
    div2 = []
    n = 1
    while n < a:

        c = a % n
        if c == 0:
            div1.append(n)
        n = n + 1
    m = 1
    while m < b:

        d = b % m
        if d == 0:
            div2.append(m)
        m = m + 1

    if sum(div1) == b and sum(div2) == a:
        return True
    else:
        return False
           