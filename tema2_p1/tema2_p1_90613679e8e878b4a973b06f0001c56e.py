# por favor escribe aquí tu función
def es_primo(numero):
    if numero == 1:
        return False
    for n in range(2, numero+1):
        if numero % n == 0 and n != numero:
            return False
        elif numero % n == 0 and n == numero:
            return True
        else:
            return True

if __name__=="__main__":
    numero = int(input("Ingrese su numero : "))
    print(es_primo(numero))


