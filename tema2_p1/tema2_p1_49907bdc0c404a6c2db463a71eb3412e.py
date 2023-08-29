# por favor escribe aquí tu función
def es_primo(numero):
    contado=0
    for i in range (1,numero+1):
     if numero%i==0 :
        contado+=1

    if contado==2:
        return True
    else:
            return False