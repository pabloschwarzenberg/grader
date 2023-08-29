# completa el código de la función
def amigos(a,b):
    sumaA = 0
    sumaB = 0
    contadorA = 1
    contadorB = 1
    while contadorA<=a:
        if a%contadorA==0:
            sumaA= sumaA + contadorA
        contadorA= contadorA+1
    while contadorB<=b:
        if b%contadorB==0:
            sumaB= sumaB + contadorB
        contadorB= contadorB+1
    if sumaA==sumaB: return True
    else: return False
           