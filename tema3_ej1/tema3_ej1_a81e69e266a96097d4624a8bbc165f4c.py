# completa el código de la función
def suma_divisores(j):
    until = 0
    for x in range(1,j-1):
        resto = j%x
        if resto!=0:
            continue
        until = until+x
    if until==1:
        wap=True
    else:
        wap=False

    return until, wap