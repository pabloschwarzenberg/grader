def suma_divisores(numero):
    divisor = 1
    resultado = False
    sumadivisores = 0
    contadordivisores = 0
    while divisor < numero:
        if numero%divisor==0:
            contadordivisores += 1
            sumadivisores += divisor
            divisor += 1
        else:
            divisor += 1
    if contadordivisores==1:
        resultado = True
    return sumadivisores,resultado