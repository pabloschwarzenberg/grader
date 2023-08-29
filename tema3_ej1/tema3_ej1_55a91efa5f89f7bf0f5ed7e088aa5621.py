# completa el código de la función
def suma_divisores(x):
    contador = 0    
    i = 1
    while i < x:
        if x%i == 0:
            contador =+ 1
        i =+ 1
    if contador == 1:
        return(contador, True) 
    else:
        return(contador, False)