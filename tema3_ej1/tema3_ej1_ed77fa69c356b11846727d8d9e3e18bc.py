def suma_divisores(a):    
    div = 0
    for n in range(1,a):
        if a % n == 0:
            div = div + n
            continue
        
        else:
            continue

    if div == 1:       
        return div, True

    else:
        return div, False