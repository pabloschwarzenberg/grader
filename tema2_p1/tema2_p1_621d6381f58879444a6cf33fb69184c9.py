# por favor escribe aquí tu función
def es_primo(numero):
    Numero=int(input("Ingresa un numero: "))
    reciproco=Numero%Numero-1
    if reciproco!=0:
        print("No es primo")
    else:
        return