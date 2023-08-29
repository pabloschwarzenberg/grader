# completa el código de la función
def suma_divisores(n):
    ds = []
    for i in range(1, n):
        if n%i == 0:
            i = ds.append(i)
    s = 0
    for d in ds:
        s = s + d
    if s == 1:
        ep = True
        return s, ep
    else:
        ep = False
        return s, ep