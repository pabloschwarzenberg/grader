# por favor escribe aquí tu función
def es_primo(numero):
    if numero==1:
        return(False)
    contador=0
    for i in range(2,numero-2):
        if numero%i==0:
            contador=contador+1
    if contador>0:
        return(False)
    return(True)
           