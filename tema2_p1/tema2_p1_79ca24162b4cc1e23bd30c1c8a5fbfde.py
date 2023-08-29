# por favor escribe aquí tu función
def es_primo(numero):
    suma=0
    for i in range(1,numero):
        if numero%i==0:
            suma=suma+i
    if suma==1:
        return True
    else:
        return False