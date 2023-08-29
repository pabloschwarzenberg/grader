def es_primo(numero):
    if numero != 1:
        for n in range(2, numero):
            if numero % n == 0:
                print('No es primo, es compuesto')
                return False
            print('Es primo')
            return True
    else:
        return False