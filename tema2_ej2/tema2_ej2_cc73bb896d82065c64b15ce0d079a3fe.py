# completa el código de la función
def amigos(a,b):
    contadora = 0
    contadorb = 0
    for listaa in range(1,a):
        if a%listaa==0:
            contadora +=listaa
    if contadora !=b:
        return(False)
    for listab in range(1,b):
        if b%listab == 0:
            contadorb += listab
    if contadorb != a:
        return(False)
    return(True)

           