def numero_perfecto(num):
    i = 1
    aux = 0
    backer = 0
    while i < num:
        if num % i == 0:
            o = aux
            aux = i
            if o < i:
                sumsum = aux + backer
                backer = sumsum
        i += 1
    
    return sumsum == num