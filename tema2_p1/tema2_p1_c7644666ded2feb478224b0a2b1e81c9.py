def es_primo(numero):

    contador = 0
    divisor = 1
    contadorb = 0
    
    while contador < numero : 
        if (numero % divisor) == 0:
            contadorb = contadorb + 1
            
            
        divisor = divisor + 1
        contador = contador + 1
    
    if contadorb == 2:
        mensaje = True
    else:
        mensaje = False

    return mensaje