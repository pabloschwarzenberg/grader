a = 8
def suma_divisores(a):
    m = 0
    s = 0
    j = []
    d = a
    while m < a :
        m = m + 1
        a = d
        if a%m == 0:
            r = int(a/m)
            j.append(r)
    del (j[0])
    jj = set(j)
    for i in jj:
        s = s + i
    if s == 1:
        return s, True
    elif s != 1:
        return s, False
print(suma_divisores(a))




