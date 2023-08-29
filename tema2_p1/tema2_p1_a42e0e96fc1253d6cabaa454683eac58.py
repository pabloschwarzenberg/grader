def es_primo(numero):
    validador=True
    if numero==1:
        validador=False
        return validador
    elif numero==2:
        return validador
    for i in range(2,numero):
        if (numero%i)==0:
            validador=False
    return validador
    