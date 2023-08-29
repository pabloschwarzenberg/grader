# por favor escribe aquí tu función
def es_primo(numero):
    if numero != 1:
        for a in range(2,numero):
        #Para que un número sea primo, este no debe ser divisible por ningún numero en el rango especificado
            if (numero%a) == 0:
                return False

            else:
                return True
    else:
        return False
        