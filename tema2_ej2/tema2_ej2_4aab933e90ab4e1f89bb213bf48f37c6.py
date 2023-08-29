def amigos(a,b):
    sumaa =0
    sumab =0
    for x in range(1,a):
        if a%x==0:
            sumaa +=x
    if sumaa !=b:
        return(False)
    for d in range(1,b):
        if b%d==0:
            sumab +=d
    if sumab !=a:
        return(False)
    return(True)

