# completa el código de la función

def suma_divisores(a):
    x = a - 1
    valor = 0
    while (x > 0):
        if a % x == 0:
            valor += x
        x = x - 1
    if valor != 1:
        return(valor , False)
    else:
        return(valor , True)
