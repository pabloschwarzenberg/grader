def numero_perfecto(a):
    numero=0
    for i in range(1,a-1):
        if (a % i) == 0:
            numero += i
    if a == numero:
        return(True)
    else:
        return(False)
           