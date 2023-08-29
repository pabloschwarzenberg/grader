def suma_divisores(a):
    p = []
    for x in range(1, a):
        if a % x == 0:
            if a == x:
                p.append(0)
            else:
                p.append(x)
    y = False
    print(sum(p)%a)
    if sum(p) >= 1:
        if sum(p) == 1:
            y = True
        elif sum(p) == 0:
            y = True


    return(sum(p), y)