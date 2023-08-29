# completa el código de la función
def suma_divisores(a):
    i = 1
    contador = 0
    while i < a:
        if a%i == 0:
            contador = contador + i
        i = i + 1
    if contador == 1:
        return(contador, True) 
    else:
        return(contador, False)
           