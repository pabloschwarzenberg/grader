# por favor escribe aquí tu función
def es_primo(numero):
    if numero != 1: 
        for i in range(2,numero):
            if numero % i == 0:
                print("No es primo")
                return False
        print("Tu numero si es primo")
        return True 
    else:
        return False
