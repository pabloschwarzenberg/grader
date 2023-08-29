# por favor escribe aquí tu función
def es_primo(numero):
    X = numero % 2
    if numero == 1:
        return False
    else:
        if X == 1:
            return True
        else:
            if X == 0:
                return False
try:
    convertidor = int(input("Introduzca el numero: "))
    print(es_primo(convertidor))
except:
    print("Eso no se puede calcular")