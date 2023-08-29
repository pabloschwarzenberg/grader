a = 6
def numero_perfecto(a):
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
    if s == a:
        return True
    else: return False

print(numero_perfecto(a))




