# completa el código de la función
def suma_divisores(A):
    cont = 1
    suma = 0

    while cont != A:

        if A % cont == 0:
            suma = suma + cont

        cont += 1
      
    if suma != 1:
        return False

    if suma == 1:
        return True