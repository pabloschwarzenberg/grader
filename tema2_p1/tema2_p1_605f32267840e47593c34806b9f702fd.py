# por favor escribe aquí tu función
def es_primo(a):
    divisor = a
    if a == 1:
        return False
    if a == 2:
        return True
    if a == 3:
        return True
    else:
        for ciclo in range(a-2):
            divisor = divisor-1
            division =  a/divisor
            aprox = a//divisor
            aproxR = division / aprox
            if aproxR == 1:
                break
        if aproxR == 1:
            return False
        else:
            return True