# completa el código de la función
def suma_divisores(a):
    i = 1
    cont = 0
    while i < a:
        if a%i == 0:
            cont = cont + i
        i = i + 1
    if cont == 1:
        return(cont, True) 
    else:
        return(cont, False)
           