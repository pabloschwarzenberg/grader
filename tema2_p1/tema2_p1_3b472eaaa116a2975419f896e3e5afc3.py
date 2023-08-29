# por favor escribe aquí tu función
def es_primo(numero):
    valor=True
    if numero==1:
        valor=False
    elif numero !=2 and numero%2==0:
        valor=False
    elif numero!=3 and numero%3==0:
        valor=False

    return valor

           