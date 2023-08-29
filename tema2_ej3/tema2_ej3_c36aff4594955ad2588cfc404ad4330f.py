def numero_perfecto(a):
    n = 1
    div = 0
    while n < a:
        if a % n == 0:
            div += n
        n += 1
    if div == a:
        perf = True
    else:
        perf = False
    return perf