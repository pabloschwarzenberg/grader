# completa el código de la función
def suma_divisores(a):
   x = a - 1
    resultado = 0
    while x > 0:
        if a % x == 0:
            resultado += x
        x = x - 1
    if resultado != 1:
        return(resultado , False)
    else:
        return(resultado , True)
 
           