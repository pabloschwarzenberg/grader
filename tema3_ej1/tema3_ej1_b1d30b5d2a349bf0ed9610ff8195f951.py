def suma_divisores(r):
    y = []
    for x in range(1, r):
        if r % x == 0:
            if r == x:
                y.append(0)
            else:
                y.append(x)
    w = False
    print(sum(y)% r)
    if sum(y) >= 1:
        if sum(y) == 1:
            w = True
        elif sum(y) == 0:
            w = True


    return(sum(y), w)