# completa el código de la función
def suma_divisores(k):
    t1 = [1]
    for asd in range(2, k + 1):
        if k % asd == 0:
            print(asd)
            t1.append(asd)

    t2 = sum(t1) - k
    print(t2)

    if 0 == k % 2 or 0 == k % 3 or k == 1:
        return t2, False
    else:
        return t2, True