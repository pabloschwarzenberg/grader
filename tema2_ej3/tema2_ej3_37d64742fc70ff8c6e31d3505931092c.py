def numero_perfecto(numero):
    cont = 1
    a = 0
    while cont != numero :
        if (numero % cont) == 0 :
            a = a + cont
        cont = cont + 1
    if a == numero :
        return True
    else:
        return False