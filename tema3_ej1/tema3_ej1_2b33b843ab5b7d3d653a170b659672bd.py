def neo_divisor_x(num):
    i = 1
    aux=0
    backer=0
    while i < num:
        if num%i == 0:
            o = aux
            aux = i
            if o < i:
                sumsum = aux + backer
                backer = sumsum                                                                                                                                                                            i += 1 
    if sumsum == 1:
        isprimo = "es primo"
    else:
        isprimo = "no es primo"
    return (isprimo)