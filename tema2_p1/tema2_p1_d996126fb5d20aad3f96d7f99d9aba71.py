def es_primo(numero):

    contador=1
    divisores=0

    while contador<=numero:
        if numero%contador==0:
           divisores=divisores+1

        contador=contador+1

    if divisores==2:
        return True
    else:
        return False