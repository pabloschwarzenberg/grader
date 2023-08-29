# por favor escribe aquí tu función
# Funcion
def es_primo(numero, n=2):
    if numero != 1:
        if n >= numero:
            print(numero, "es primo")
            return True
        elif numero % n != 0:
            return es_primo(numero, n+1)
        else:
            print(numero, "no es primo")
            return False
    else:
        print(numero, "no es primo")
        return False
