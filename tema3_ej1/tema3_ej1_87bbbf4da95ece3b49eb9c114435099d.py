# completa el código de la función
def suma_divisores(a):
    esPrimo = True
    noesPrimo = False
    m = [1]
    for k in range(2, a + 1):
        if a % k == 0:
            m.append(k)
    for e in m:
        if e == a:
            m.remove(e)
    if sum(m) == 1:
        return sum(m), esPrimo
    else:
        return sum(m), noesPrimo
           