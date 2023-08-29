# completa el código de la función
def amigos(n1, n2):
    c_n1 = 0
    c_n2 = 0

    for i in range(1, n1):
        if n1%i==0:
            c_n1 = c_n1+i

    for i in range(1, n2):
        if n2%i==0:
            c_n2 = c_n2+i

    if c_n1==n2 and c_n2==n1:
        return True
    else:
        return False           