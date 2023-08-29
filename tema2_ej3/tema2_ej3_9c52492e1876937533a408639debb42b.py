def numero_perfecto(a):
    total=0
    divisores=[]
    for i in range (1,a):
        if a%i == 0:
            divisores.append(i)
    for j in divisores:
        total=total+j
    if total == a:
        return(True)
    return(False)