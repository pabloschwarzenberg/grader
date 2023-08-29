def numero_perfecto(a):
    divisores = 0
    p = 1
    while p < a:
        if a//p == a/p and p != 0:
            divisores = divisores + p
        p += 1
    return bool(divisores == a)
           