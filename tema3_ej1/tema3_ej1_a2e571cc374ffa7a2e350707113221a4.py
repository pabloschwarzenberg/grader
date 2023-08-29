# completa el código de la función
def suma_divisores(a):
    cont = 0
    suma = 0
    while cont < a:
        try:
            if a%cont == 0:
                suma += cont
        except ZeroDivisionError:
            pass
        cont+= 1
    if suma == 1:
        return suma , True
    if suma != 1:
        return suma, False
