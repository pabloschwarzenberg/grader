def es_primo(Numero):
    lista = [2, 3, 5, 7, 11]
    esprimo = True
    contador = 0
    for numeros in lista:
        if  Numero <= numeros:
            break
        divicion = Numero % numeros
        if divicion == 0:
            contador += 1
        
    if contador >= 1:
        esprimo = False
    if Numero == 1:
        esprimo = False
    return esprimo
